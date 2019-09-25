from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)


class Seller(models.Model):
    company_name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
