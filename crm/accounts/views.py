from django.shortcuts import render
from django.http import HttpResponse
from .models import * 
 
all_cust=customer.objects.all()
# Create your views here.
def index(request):
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


def Products(request, c_id):
    prod_data= products.objects.all()
    return render(request, 'accounts/products.html',{'prod_data': prod_data})

