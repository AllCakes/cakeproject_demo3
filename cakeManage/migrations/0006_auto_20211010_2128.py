# Generated by Django 3.2.5 on 2021-10-10 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeManage', '0005_ordertransaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordertransaction',
            name='type',
        ),
        migrations.AddField(
            model_name='ordertransaction',
            name='success',
            field=models.BooleanField(default=False),
        ),
    ]