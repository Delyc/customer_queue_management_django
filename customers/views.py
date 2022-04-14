from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
import random
from .models import Customer, Teller

def index(request):
    tellers = Teller.objects.all()

    return render(request, "index.html", context={"tellers":tellers})

def teller_view(request, pk):
    teller = get_object_or_404(Teller, id=pk)
    if teller:
        customers = teller.get_customers()
        waiting_time= teller.get_estimated_time()
        return render(request, "teller.html", context={"teller": teller, "customers": customers})
    return HttpResponse('Not found')

def register_customer(request, pk):
    teller = get_object_or_404(Teller, id=pk)
    name = request.GET.get("name", "Un-named")
    customer = Customer()
    customer.name = name
    customer.teller = teller
    customer.save()
    return redirect(teller)
def delete_customer(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    teller = customer.teller
    customer.delete()
    return redirect(teller)




