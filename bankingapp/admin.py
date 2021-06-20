from django.contrib import admin
from bankingapp.models import Customer

admin.site.register(Customer)


class Customer(admin.ModelAdmin):
    list_display = ('customer_name', 'account_no', 'current_balance')