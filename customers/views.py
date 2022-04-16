from django.core import serializers
import json
import random
from datetime import datetime, timedelta

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from pkg_resources import safe_extra

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
        customers = customer_clean(teller.get_customers())
        customers = teller.get_customers()
        next_customer = teller.get_next_customer()
        millisec = datetime.now().isoformat()
        now = datetime.now().isoformat()
        if next_customer:
            millisec = next_customer.expired_date.isoformat()

        return render(request, "teller.html", context={"teller": teller, "customers": customers, "next_time": millisec, "current_time": now})
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
    if not customer:
        return HttpResponse({"delete": True})
    customer.delete()
    return HttpResponse({"delete": False})


def get_waiting_time(request, pk):
    teller = get_object_or_404(Teller, id=pk)
    if teller:
        now = datetime.now()
        serializer = serializers.serialize(
            "json", teller.get_customers())
        next_customer = teller.get_next_customer()
        if next_customer:
            next_customer = {
                "name": next_customer.name,
                "code": next_customer.code,
                "arrived_at": next_customer.arrived_at.isoformat()
            }
            data = {
                "customers": serializer,
                "next_customer": next_customer,
                "success": True
            }
            return JsonResponse(json.dumps(data), safe=False)

        return JsonResponse({
            "success": False,
            "reason": "No more customers"
        })
    return JsonResponse({
        "success": False,
        "reason": "Teller not found"
    })
