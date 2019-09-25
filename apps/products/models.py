from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model


class ProductCategory(models.Model):
    name = models.CharField(max_length=20)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    seller = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    units = models.IntegerField(default=0)
    in_stock = models.BooleanField()
    discount = models.IntegerField(
        default=0, validators=[MaxValueValidator(100), MinValueValidator(0)]
    )

    def save(self, *args, **kwargs):
        if self.units > 0:
            self.in_stock = True
        else:
            self.in_stock = False
