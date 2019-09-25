from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    email = models.EmailField(max_length=254, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Seller(models.Model):
    company_name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
