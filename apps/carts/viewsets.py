from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
import io
from rest_framework.parsers import JSONParser
from django.db.models import Prefetch

from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer, OrderItemserializer
from apps.orders.serializers import OrderSerializer
from apps.products.models import Product


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAdminUser | IsAuthenticated]

    def list(self, request, *args, **kwargs):

        if request.user.is_customer:
            cart = Cart.objects.filter(user_id=request.user.id, is_paid=False).last()
            serializer = CartSerializer(cart)
            return Response(serializer.data)

        if request.user.is_seller or request.user.is_superuser:
            # OLD SOLUTION HERE FOR FUTURE REF
            # carts = Cart.objects.filter(is_paid=True).prefetch_related(
            #     Prefetch(
            #         "cartitems",
            #         queryset=CartItem.objects.filter(
            #             product__seller_id=request.user.id
            #         ),
            #     )
            # )

            carts_id = Cart.objects.filter(is_paid=True).values_list("id", flat=True)

            cartitems = CartItem.objects.filter(
                cart_id__in=carts_id, product__seller_id=request.user.id
            ).prefetch_related("cart__user__customer")

            serializer = OrderItemserializer(cartitems, many=True)
            return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if "id" in request.data:
            cart = Cart.objects.get(pk=request.data["id"])
        else:
            cart = Cart.objects.create(user_id=request.user.id, total_price=0)

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

        cart.is_paid = True
        cart.save()

        serializer.save(cart=cart)

        return Response(serializer.data)
