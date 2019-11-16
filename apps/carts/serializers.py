from rest_framework import serializers

from .models import CartItem, Cart
from apps.products.serializers import ProductSerializer


class OrderItemserializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(required=False, source="product.id")
    product_name = serializers.CharField(required=False, source="product.name")
    product_decription = serializers.CharField(
        required=False, source="product.description"
    )
    user = serializers.CharField(required=False, source="cart.user.first_name")

    class Meta:
        model = CartItem
        fields = (
            "id",
            "product_id",
            "product_name",
            "product_decription",
            "user",
            "shipping_address",
        )


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

