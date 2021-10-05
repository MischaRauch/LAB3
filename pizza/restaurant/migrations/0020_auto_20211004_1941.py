# Generated by Django 3.0.5 on 2021-10-04 19:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0019_auto_20211004_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='time_when_employee_left',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 4, 19, 41, 56, 53189), verbose_name='orderedTime'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 4, 19, 41, 56, 53502), verbose_name='orderedTime'),
        ),
    ]
