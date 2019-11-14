from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer
from .models import Order


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, user_pk=None, *args, **kwargs):
        if request.user.id != int(user_pk):
            return Response(
                {"error": "You are not authorized to access this resource"}, 401
            )

        queryset = Order.objects.filter(user=user_pk)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)
