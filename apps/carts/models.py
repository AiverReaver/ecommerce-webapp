from django.db import models
from apps.users.models import User
from apps.products.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="cartitems", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="product", on_delete=models.CASCADE
    )
    quantity = models.PositiveSmallIntegerField()
