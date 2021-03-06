import uuid
from django.db import models
from apps.carts.models import Cart
from apps.users.models import User


class Order(models.Model):
    order_number = models.UUIDField(default=uuid.uuid4, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="users", on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    paymant_date = models.DateTimeField(auto_now=True, auto_now_add=False)
