from rest_framework import generics
from rest_framework.views import APIView
from .serializers import ItemSerializer, TransactionRetrieveSerializer,TransactionCreateSerializer
from .models import Item,OrderItem, Transaction
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from datetime import datetime
from django.db.models import Sum,F,Count,Avg
import pandas as pd



class ItemListView(generics.ListAPIView): 
    serializer_class = ItemSerializer
    queryset = Item.objects.all()



class TransactionCreateView(generics.CreateAPIView): 
    serializer_class = TransactionCreateSerializer
    queryset = Transaction.objects.all()




class TransactionRetrieveView(generics.RetrieveAPIView): 
    serializer_class = TransactionRetrieveSerializer
    queryset = Transaction.objects.all()




class TransactionByDayView(APIView): 
    def get(self, request, *args, **kwargs):
        date_string = request.data.get("date")
        date=datetime.strptime(date_string,"%d/%m/%Y")

        total_sales=Transaction.objects.filter(date__contains=date.date()).aggregate(sales=Sum(F('items__quantity')*F('items__item__price')))
        no_of_transactions=Transaction.objects.filter(date__contains=date.date()).count()
        total_quantity_items_sold=Transaction.objects.filter(date__contains=date.date()).aggregate(Sum('items__quantity'))
        total_quantity_items_sold_for_each_item=Transaction.objects.filter(date__contains=date.date()).values('items__item__title').annotate(Sum('items__quantity'))
        total_quantity_items_sold_for_each_item=Transaction.objects.filter(date__contains=date.date()).values('items__item__title').annotate(Sum('items__quantity'))
        total_quantity_sold_in_each_item_category=Transaction.objects.filter(date__contains=date.date()).values('items__item__category__name').annotate(Sum('items__quantity'))
        total_sales_amount_in_each_item_category=Transaction.objects.filter(date__contains=date.date()).values('items__item__category__name').annotate(sales=Sum(F('items__quantity')*F('items__item__price')))

        res={
            "total_sales":total_sales,
            "no_of_transactions":no_of_transactions, 
            "total_quantity_items_sold":total_quantity_items_sold,
            "total_quantity_items_sold_for_each_item":total_quantity_items_sold_for_each_item, 
            "total_quantity_sold_in_each_item_category":total_quantity_sold_in_each_item_category, 
            "total_sales_amount_in_each_item_category":total_sales_amount_in_each_item_category
        }
        return Response(res, status=HTTP_200_OK)






class TransactionByDateRangeView(APIView): 
    def get(self, request, *args, **kwargs):
        start_date_string = request.data.get("start_date")
        end_date_string = request.data.get("end_date")

        start_date=datetime.strptime(start_date_string,"%d/%m/%Y")
        end_date=datetime.strptime(end_date_string,"%d/%m/%Y")
        delta=(end_date-start_date).days

        total_sales=Transaction.objects.filter(date__range=[start_date,end_date]).aggregate(sales=Sum(F('items__quantity')*F('items__item__price'))/delta)
        no_of_transactions=Transaction.objects.filter(date__range=[start_date,end_date]).count()
        total_quantity_items_sold=Transaction.objects.filter(date__range=[start_date,end_date]).aggregate(Sum('items__quantity'))
        total_quantity_items_sold_for_each_item=Transaction.objects.filter(date__range=[start_date,end_date]).values('items__item__title').annotate(quantity=Sum('items__quantity')/delta)
        total_quantity_sold_in_each_item_category=Transaction.objects.filter(date__range=[start_date,end_date]).values('items__item__category__name').annotate(quantity=Sum('items__quantity')/delta)
        total_sales_amount_in_each_item_category=Transaction.objects.filter(date__range=[start_date,end_date]).values('items__item__category__name').annotate(sales=Sum(F('items__quantity')*F('items__item__price'))/delta)

        res={
            "total_sales":total_sales,
            "no_of_transactions":no_of_transactions, 
            "total_quantity_items_sold":total_quantity_items_sold,
            "total_quantity_items_sold_for_each_item":total_quantity_items_sold_for_each_item, 
            "total_quantity_sold_in_each_item_category":total_quantity_sold_in_each_item_category, 
            "total_sales_amount_in_each_item_category":total_sales_amount_in_each_item_category
        }
        return Response(res, status=HTTP_200_OK)







class TestView(APIView): 

    def get(self, request, *args, **kwargs):
        
        date_string = "6/6/2022"
        date=datetime.strptime(date_string,"%d/%m/%Y")

        transaction_qs=Transaction.objects.filter(date__contains=date.date()).prefetch_related('items__item')
        
        ot=OrderItem.objects.values('item__category__name','quantity')
        t_qs2=Transaction.objects.filter(date__contains=date.date()).values('items__item__category__name').annotate(Sum('items__quantity'))

        
        print(t_qs2)
        
        return Response(status=HTTP_200_OK)

