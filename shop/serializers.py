from rest_framework import serializers
from .models import Category,Item,OrderItem,Transaction

class CategorySerializer(serializers.ModelSerializer): 
    class Meta:
        model = Category
        fields = ('name','description',)



class ItemSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Item
        fields = ('item_code','title','price','category','description','available_quantity',)



class OrderItemResponseSerializer(serializers.ModelSerializer): 
    total_item_price = serializers.ReadOnlyField()
    item = serializers.StringRelatedField()
    class Meta:
        model = OrderItem
        fields = ('item','quantity','total_item_price',)





class TransactionRetrieveSerializer(serializers.ModelSerializer):
    items= OrderItemResponseSerializer(many=True)
    total = serializers.ReadOnlyField()
    class Meta:
        model = Transaction
        fields = ('id','items','date','created_on','completed','total')







class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('item','quantity',)


class TransactionCreateSerializer(serializers.ModelSerializer):
    items = OrderItemCreateSerializer(many=True)

    class Meta:
        model = Transaction
        fields = ('items',)

    def create(self, validated_data):
        items_data = validated_data.pop('items')
       
        transaction = Transaction.objects.create(
            **validated_data,
            )
        print(transaction)
        for item_data in items_data:
            order_item=OrderItem.objects.create(**item_data)
            transaction.items.add(order_item)
            order_item.item.available_quantity-=order_item.quantity
            order_item.item.save()

        transaction.completed = True
        transaction.save()
        return transaction

