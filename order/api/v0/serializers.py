from rest_framework import serializers
from django.db.models import Sum


from order.models import Order , OrderItem
from product.models import Image

class OrderItemSerializer(serializers.ModelSerializer):
    product_title = serializers.CharField(source='product.title')
    product_price = serializers.IntegerField(source='product.price')
    main_image = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = [ 'product_title', 'product_price', 'main_image' , 'quantity' , 'total_price']

    def get_main_image(self, obj):
        main_image = Image.objects.filter(product = obj.product).first()
        if main_image:
            return main_image.image.url
        return ""

class OrderSerializer(serializers.ModelSerializer):
    orderitems = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['pk' , 'total_price' , 'orderitems']

    def get_orderitems(self, obj):
        orderitems = OrderItem.objects.filter(order = obj.id)
        serializer = OrderItemSerializer(orderitems, many=True)
        return serializer.data



class CreateOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderItemDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['pk', 'product', 'quantity']