import random
from datetime import datetime, timedelta
from distutils.command.upload import upload
from time import timezone

from django.db import models
from django.urls import reverse


def gen_id():
    month = datetime.now().strftime("%m-%d-%Y")

    number = random.randint(1000, 9999)
    return "%s-%s" % (month, number)


class Customer(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    code = models.CharField(max_length=255)
    arrived_at = models.DateTimeField(auto_now_add=True)
    teller = models.ForeignKey("Teller", on_delete=models.CASCADE)
    expired_date = models.DateTimeField(
        auto_now_add=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = gen_id()
        if not self.expired_date:
            now = datetime.now()
            future = now + timedelta(minutes=self.teller.wait_time)
            print(future, now)
            print(future > now)
            self.expired_date = future
        super().save(*args, **kwargs)

    def __str__(self):
        return "%s-%s" % (self.name, self.code)

    class Meta:
        ordering = ["-arrived_at"]

    def get_delete_url(self):

        return reverse("delete", kwargs={"pk": self.pk})


class Teller(models.Model):
    name = models.CharField(max_length=30)
    wait_time = models.PositiveIntegerField(default=1)
    profile = models.ImageField(upload_to="profile", default="avatar.png")
    completion_time = models.DateTimeField(
        auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_customers(self):
        customers = self.customer_set.all().order_by("arrived_at")
        return customers

    def customers(self):
        customers = self.customer_set.all().count()
        return customers

    def get_estimated_time(self):
        customers = self.customer_set.all().count()

        return customers * self.wait_time

    def get_absolute_url(self):
        return reverse("teller-view", kwargs={"pk": self.pk})

    def get_register_url(self):
        return reverse("register", kwargs={"pk": self.pk})

    def get_next_customer(self):
        now = datetime.now()
        customers = self.customer_set.last()
        if customers:
            if customers.expired_date > now:
                return customers
            else:
                customers.delete()

        return None


# Create your models here.
