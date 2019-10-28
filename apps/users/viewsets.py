from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serialzers import SellerSerializer, CustomerSerializer
from .models import Seller, Customer


class CustomerViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class SellerViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [AllowAny]
