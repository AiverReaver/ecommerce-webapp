from rest_framework import serializers

from .models import Product, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # initialize fields
        fields = kwargs.pop("fields", None)
        super(ProductSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    class Meta:
        model = Product
        fields = ("id", "name", "name", "description", "price", "in_stock", "discount")


class ProductCategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return ProductCategory.objects.create(**validated_data)

    class Meta:
        model = ProductCategory
        fields = ("id", "name", "products")

