# Generated by Django 3.2.5 on 2022-02-03 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cakeManage', '0005_auto_20220203_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cake',
            name='색',
        ),
        migrations.RemoveField(
            model_name='cake',
            name='색가격',
        ),
        migrations.RemoveField(
            model_name='cake',
            name='크림종류',
        ),
        migrations.RemoveField(
            model_name='cake',
            name='크림종류가격',
        ),
    ]
