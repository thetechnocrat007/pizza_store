from django.contrib import admin
from .models import Item,OrderItem,Transaction,Category
# admin.site.register(Item)
admin.site.register(OrderItem)
# admin.site.register(Transaction)
admin.site.register(Category)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display=('id','date','created_on','completed')


@admin.register(Item)
class TransactionAdmin(admin.ModelAdmin):
    list_display=('item_code','title','price','category','available_quantity')