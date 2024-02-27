from django.db import models
from shop.models import Shop

class Order(models.Model):

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    order_date = models.DateTimeField('date ordered', auto_now_add=True)
    address = models.CharField(max_length=40)
    delivery_finish = models.BooleanField(default=False)
