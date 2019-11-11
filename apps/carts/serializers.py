from rest_framework import serializers

from .models import CartItem, Cart
from apps.products.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ("id", "product")


class CartSerializer(serializers.ModelSerializer):

    cartitems = CartItemSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return Cart.objects.create(**validated_data)

    class Meta:
        model = Cart
        fields = ("id", "total_price", "cartitems")

