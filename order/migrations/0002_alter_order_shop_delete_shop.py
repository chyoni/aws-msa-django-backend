# Generated by Django 5.0.2 on 2024-02-27 02:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop'),
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
    ]
