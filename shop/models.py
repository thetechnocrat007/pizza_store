from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.utils import timezone
from .utils import getBusinessDate


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    item_code=models.CharField(primary_key=True,max_length=3)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ForeignKey(Category, blank=True, null=True ,on_delete=models.SET_NULL)
    description = models.TextField(blank=True, null=True)
    available_quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.title






class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    # created_on = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.item.title 

    @property
    def total_item_price(self):
        return self.quantity * self.item.price





class Transaction(models.Model):
    items = models.ManyToManyField(OrderItem)
    date = models.DateTimeField(default=getBusinessDate)
    
    created_on = models.DateTimeField(auto_now_add=True)
    # created_on = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)

    @property
    def total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.total_item_price
        return total

    
