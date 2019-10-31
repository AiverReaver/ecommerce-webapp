from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Cart
from .serializers import CartSerializer
from apps.orders.serializers import OrderSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAdminUser | IsAuthenticated]

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
