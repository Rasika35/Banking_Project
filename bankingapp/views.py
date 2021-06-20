from django.contrib import messages
from django.core.exceptions import FieldError
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from bankingapp.models import Customer


class Homepage(View):
    template_name = "bankingapp/hompage.html"

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class ViewAllCustomers(View):
    template_name = "bankingapp/view_all_customers.html"

    def get(self, request):
        customers = Customer.objects.all()
        context = {"customers": customers}
        return render(request, self.template_name, context)


class CustomerDetail(View):
    template_name = "bankingapp/customer_detail.html"

    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        context = {"customer": customer}
        return render(request, self.template_name, context)


class TransferMoney(View):
    template_name = "bankingapp/transfer_money.html"

    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        print(customer)
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        customer_name = request.POST['customer_name'].lower()
        bank = request.POST['bank'].lower()
        branch = request.POST['branch'].lower()
        account_no = request.POST['account_no']
        amount = float(request.POST['amount'])

        if Customer.objects.filter(bank_name=bank, branch=branch, account_no=account_no, customer_name=customer_name).exists():

            sender_account = Customer.objects.get(pk=pk)

            if sender_account.current_balance < amount:
                return render(request, self.template_name, context={"error_current_balance": f"Insufficent balance, current balance is {sender_account.current_balance}"})
            else:
                # deduction
                sender_current_balance = float(sender_account.current_balance) - amount
                Customer.objects.filter(pk=pk).update(current_balance=sender_current_balance)

                receiver_account = Customer.objects.get(bank_name=bank, branch=branch, account_no=account_no,
                                                        customer_name=customer_name)
                receiver_current_balance = float(receiver_account.current_balance) + amount
                Customer.objects.filter(bank_name=bank, branch=branch, account_no=account_no,
                                        customer_name=customer_name).update(current_balance=receiver_current_balance)

                return redirect("view_all_customers")
        else:
            return render(request, self.template_name, context={"invalid_user": "Invalid User"})

