from django.urls import path
from .views import ItemListView, TestView,TransactionCreateView, TransactionCreateView,TransactionRetrieveView,TransactionByDayView,TransactionByDateRangeView

urlpatterns = [
    
    path('items', ItemListView.as_view(), name='getitems'),
    path('newtransaction', TransactionCreateView.as_view(), name='newtransaction'),
    path('transaction/<pk>', TransactionRetrieveView.as_view(), name='gettransaction'),
    path('get-tran-byday', TransactionByDayView.as_view(), name='get-tran-byday'),
    path('get-tran-byrange', TransactionByDateRangeView.as_view(), name='get-tran-byrange'),
    path('test', TestView.as_view(), name='test'),
    
]