from dataclasses import fields
from django.forms import ModelForm
from .models import *

class orderForm(ModelForm):
    class Meta:
        model=order
        fields= '__all__'

class customerForm(ModelForm):
    class Meta:
        model=customer
        fields=['name','phone', 'email']