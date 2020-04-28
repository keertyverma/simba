from django.db import models

# Create your models here.


class Shipment(models.Model):
    shop_name = models.CharField(max_length=50),
    fulfilment_method = models.CharField(max_length=15)

    def __str__(self):
        return self.shop_name
