import uuid
from django.db import models
from apps.carts.models import Cart


class Order(models.Model):
    order_number = models.UUIDField(default=uuid.uuid4, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
