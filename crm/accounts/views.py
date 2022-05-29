from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Home")


def customer(request):
    return HttpResponse("Custome")


def products(request):
    return HttpResponse("Products")

