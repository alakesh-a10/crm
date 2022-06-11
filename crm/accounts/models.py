import email
from pyexpat import model
from sre_constants import CATEGORY
from django.db import models

class customer(models.Model):
    name=models.CharField(max_length=200, null=True)
    phone=models.CharField(max_length=200, null=True)
    email=models.CharField(max_length=200, null=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class products(models.Model):
    CATEGORY=(
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor')
    )
    name=models.CharField(max_length=200, null=True)
    price=models.FloatField()
    category=models.CharField(max_length=200, null=True, choices=CATEGORY)
    description=models.CharField(max_length=200, null=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class order(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered','Delivered')
    )
    #customer
    #product
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    status=models.CharField(max_length=200, null=True, choices=STATUS)
