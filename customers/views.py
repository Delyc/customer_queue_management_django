import json
import random
from datetime import datetime, timedelta

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Customer, Teller


def customer_clean(customers):
    now = datetime.now()
    for customer in customers:
        if customer.expired_date < now:
            print(now, customer.expired_date)
            customer.delete()
    return customers


def index(request):
    tellers = Teller.objects.all()

    return render(request, "index.html", context={"tellers": tellers})


def teller_view(request, pk):
    teller = get_object_or_404(Teller, id=pk)
    if teller:
        customers = teller.get_customers()
        customers = customer_clean(customers)
        next_customer = teller.get_next_customer()
        millisec = datetime.now().isoformat()
        if next_customer:

            millisec = next_customer.expired_date.isoformat()
        return render(request, "teller.html", context={"teller": teller, "customers": customers, "next_time": millisec})
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


def get_waiting_time(request, pk):
    teller = get_object_or_404(Teller, id=pk)
    if teller:
        now = datetime.now()
        customers = teller.get_customers()
        next_customer = teller.get_next_customer()
        if next_customer:
            data = {
                "customers": customers,
                "next_customer": next_customer,
                "success": True
            }
            return JsonResponse(json.dumps(data))

        return JsonResponse({
            "success": False,
            "reason": "No more customerz"
        })
    return JsonResponse({
        "success": False,
        "reason": "Teller not found"
    })
