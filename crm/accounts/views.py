from django.shortcuts import render
from django.http import HttpResponse
from .models import * 
# Create your views here.
def index(request):
    all_orders=order.objects.all()
    delivered=order.objects.filter(status='Delivered').count()
    pending=order.objects.filter(status='Pending').count()
    t_order=all_orders.count()

    summary={'t_order':t_order,'pen':pending,'delivered':delivered}
    return render(request, "accounts/dashboard.html", summary)


def customer(request):
    return render(request, 'accounts/customer.html')


def Products(request):
    prod_data= products.objects.all()
    return render(request, 'accounts/products.html',{'prod_data': prod_data})

