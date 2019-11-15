from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from .serializers import ProductSerializer, ProductCategorySerializer
from .models import Product, ProductCategory
from apps.carts.models import Cart, CartItem
from apps.carts.serializers import CartItemSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated | IsAdminUser]

        return [permission() for permission in permission_classes]

    def list(self, request, category_pk=None):
        queryset = Product.objects.filter(category=category_pk)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, category_pk=None, *args, **kwargs):

        if not request.user.is_seller:
            return Response({"error": "unautorized"}, 401)
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            category = ProductCategory.objects.get(pk=category_pk)
            serializer.save(seller=request.user, category=category)
            return Response(serializer.data)

        return Response(serializer.errors, 404)


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]
