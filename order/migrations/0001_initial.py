# Generated by Django 5.0.2 on 2024-02-27 02:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=20)),
                ('shop_address', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(verbose_name='date ordered')),
                ('address', models.CharField(max_length=40)),
                ('delivery_finish', models.BooleanField(default=False)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.shop')),
            ],
        ),
    ]