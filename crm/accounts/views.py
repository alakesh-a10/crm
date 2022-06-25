from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * 
from .forms import *
 

# Create your views here.
def index(request):
    all_cust=customer.objects.all()
    all_orders=order.objects.all()
    delivered=order.objects.filter(status='Delivered').count()
    pending=order.objects.filter(status='Pending').count()
    t_order=all_orders.count()
    summary={'t_order':t_order,'pen':pending,'delivered':delivered,'all_orders':all_orders,'all_cust':all_cust}
    return render(request, "accounts/dashboard.html", summary)


def Customer(request, c_id):
    c_data=customer.objects.get(id=c_id)
    c_order=c_data.order_set.all()
    t_order=c_order.count()
    context={'c_data':c_data,'c_order':c_order,'t_order': t_order}
    return render(request, 'accounts/customer.html',context)


def Products(request):
    prod_data= products.objects.all()
    return render(request, 'accounts/products.html',{'prod_data': prod_data})


def createOrder(request):   
    if request.method=='POST':
        form_data=orderForm(request.POST)
        if form_data.is_valid:
            form_data.save()
            return redirect('/')

    Order_form=orderForm()
    context={'Order_form':Order_form}
    return render(request, 'accounts/order_form.html',context)

def updateOrder(request, o_id):
    o_data=order.objects.get(id=o_id)
    Order_form=orderForm(instance=o_data)
    context={'Order_form':Order_form}
    if request.method=='POST':
        update_data=orderForm(request.POST, instance=o_data)
        if update_data.is_valid:
            update_data.save()
            return redirect('/')
    return render(request, 'accounts/order_form.html', context)

def createCustomer(request):
    c_data=customerForm()
    if request.method=='POST':
        new_cast=customerForm(request.POST)
        if new_cast.is_valid:
            new_cast.save()
            return redirect('/')

    context={'c_data':c_data}
    return render(request, 'accounts/cust_form.html', context)

def updateCustomer(request, c_id):
    c_data=customer.objects.get(id=c_id)
    cust_form=customerForm(instance=c_data)
    if request.method=='POST':
        new_cust=customerForm(request.POST, instance=c_data)
        if new_cust.is_valid:
            new_cust.save()
            return redirect('/')
    context={'c_data':cust_form}
    return render(request, 'accounts/cust_form.html', context)

def deleteOrder(request, o_id):
    o_data=order.objects.get(id=o_id)
    context={'item':o_data}
    if request.method=='POST':
        o_data.delete()
        return redirect('/')
    return render(request, 'accounts/delete.html', context) 