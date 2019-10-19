from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .models import User
from .serialzers import SellerSerializer, CustomerSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
def register_customer(request):
    serializer = CustomerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)


@api_view(["POST"])
@permission_classes([AllowAny])
def register_seller(request):
    serializer = SellerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)
