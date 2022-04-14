from django.db import models


class Customers(models.Model):
    teller = models.CharField(max_length=50, blank=True, null=True)
    customers=models.IntegerField(blank=False, default=0)
    wait_time = models.IntegerField(default=5)

    def __str__(self):
        return self.teller
    def add_customer(self):
        customers = self.customers + 1
        self.customers = customers
        self.save()
    def remove_customer(self):
        if self.customers <= 0:
            pass
        else:
            customers = self.customers - 1
            self.customers = customers
            self.save()
    def get_estimated_time(self):
        return self.customers * self.wait_time


# Create your models here.
