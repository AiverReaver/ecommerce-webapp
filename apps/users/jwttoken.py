from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        if user.is_superuser:
            token["role"] = "admin"
        elif user.is_seller and not user.is_customer:
            token["role"] = "seller"
        elif not user.is_seller and user.is_customer:
            token["role"] = "customer"
        else:
            token["role"] = "anonymous"
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
