from django.db import models


class Customer(models.Model):
    bank_name = models.CharField(max_length=100,)
    branch = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    account_no = models.CharField(max_length=15, unique=True)
    current_balance = models.DecimalField(max_digits=100, decimal_places=2)

    def save(self, *args, **kwargs):
        self.bank_name = self.bank_name.lower()
        self.branch = self.branch.lower()
        self.customer_name = self.customer_name.lower()
        return super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return self.customer_name