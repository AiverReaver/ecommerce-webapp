from rest_framework import serializers
from .models import Order
from apps.carts.serializers import CartSerializer

class OrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer(read_only=True)
    class Meta:
        model = Order
        fields = ("id", "order_number", "cart")
