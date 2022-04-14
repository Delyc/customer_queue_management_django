from django.http import HttpResponse
from django.shortcuts import redirect, render
import random
from .models import Customers

def index(request):
    customerModel = Customers.objects.all()[0]
    if not customerModel:
        return HttpResponse("No customer we have")
    return render(request, "index.html", context={"estimated_time":customerModel.get_estimated_time(), "customers":customerModel.customers, "teller": customerModel})


def register_customer(request):
    customerModel = Customers.objects.all()[0]
    customerModel.add_customer()
    return redirect("/")
def delete_customer(request):
    customerModel = Customers.objects.all()[0]
    customerModel.remove_customer()
    return redirect("/")
# Create your views here.
