from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
import io
from rest_framework.parsers import JSONParser

from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from apps.orders.serializers import OrderSerializer
from apps.products.models import Product


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAdminUser | IsAuthenticated]

    def list(self, request, *args, **kwargs):
        cart = Cart.objects.filter(user_id=request.user.id, is_paid=False).last()
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if "id" in request.data:
            cart = Cart.objects.get(pk=request.data["id"])
        else:
            cart = Cart.objects.create(user_id=request.user.id)

        serializer = CartItemSerializer(data=request.data)

        if serializer.is_valid():
            product = Product.objects.get(pk=request.data["productId"])
            cart.total_price += product.price
            cart.save()
            serializer.save(cart=cart, product=product)
            cart_serialzier = CartSerializer(cart)
            return Response(cart_serialzier.data)
        else:
            return Response(serializer.errors)

    def destroy(self, request, pk=None, *args, **kwargs):
        cart = Cart.objects.get(pk=pk).delete()
        return Response()

    @action(detail=True, methods=["POST"])
    def checkout(self, request, pk=None):
        cart = Cart.objects.get(pk=pk)

        if request.user.id != cart.user_id:
            return Response({"detail": "Unauthorized"}, 401)

        serializer = OrderSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save(cart=cart)

        return Response(serializer.data)
