from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .models import User
from .serialzers import UserSerializer, SellerSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
def register_customer(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(first_name=request.data["name"])
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
