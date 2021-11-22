# Generated by Django 3.2.5 on 2021-11-05 03:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeManage', '0007_merge_0004_store_price_0006_auto_20211010_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='price',
            field=models.IntegerField(default=90000, validators=[django.core.validators.MinValueValidator(0, django.core.validators.MaxValueValidator(100000))]),
        ),
    ]