from django.db import models

class Shop(models.Model):

    shop_name = models.CharField(max_length=20)
    shop_address = models.CharField(max_length=40)