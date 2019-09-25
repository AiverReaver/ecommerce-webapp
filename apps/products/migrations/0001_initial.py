# Generated by Django 2.2.5 on 2019-09-25 14:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('units', models.IntegerField(default=0)),
                ('in_stock', models.BooleanField()),
                ('discount', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ProductCategory')),
            ],
        ),
    ]
