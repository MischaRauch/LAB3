# Generated by Django 3.0.5 on 2021-10-04 17:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0021_auto_20211004_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='time_when_employee_left',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 4, 19, 43, 23, 113870), verbose_name='orderedTime'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 4, 19, 43, 23, 114149), verbose_name='orderedTime'),
        ),
    ]
