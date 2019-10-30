from rest_framework import serializers

from .models import User, Seller, Customer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email")


class SellerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    def create(self, validated_data):
        validated_user = validated_data.pop("user")
        user = User.objects.create_user(
            is_customer=False, is_seller=True, **validated_user
        )
        return Seller.objects.create(user=user, **validated_data)

    class Meta:
        model = Seller
        fields = ("id", "company_name", "user")


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    def create(self, validated_data):
        validated_user = validated_data.pop("user")
        user = User.objects.create_user(
            is_customer=True, is_seller=False, **validated_user
        )
        return Customer.objects.create(user=user, **validated_data)

    class Meta:
        model = Customer
        fields = ("id", "user")
