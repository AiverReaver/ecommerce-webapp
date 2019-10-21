from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class EmailUserManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=150)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = EmailUserManager()


class Seller(models.Model):
    company_name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ship_address = models.CharField(max_length=300, blank=True)
    ship_city = models.CharField(max_length=20, blank=True)
    ship_country = models.CharField(max_length=20, blank=True)
