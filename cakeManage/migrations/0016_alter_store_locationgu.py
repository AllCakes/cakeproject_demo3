<<<<<<< HEAD
# Generated by Django 3.2.5 on 2021-11-19 14:44
=======
# Generated by Django 3.2.5 on 2021-11-19 14:43
>>>>>>> e63308283eb5b8736545facd92c7487dc61adcd1

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeManage', '0015_auto_20211119_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='locationGu',
            field=models.CharField(default='노원구', max_length=10, verbose_name='구'),
        ),
    ]
