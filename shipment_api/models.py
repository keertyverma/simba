from django.db import models

# Create your models here.


class Shipment(models.Model):
    shop_client_id = models.CharField(max_length=50, default=None)
    fulfilment_method = models.CharField(max_length=15, default=None)
    shipment_date = models.TextField(default=None)
    shipment_reference = models.TextField(default=None)
    pick_up_point = models.BooleanField(default=None)
    billing_details_first_name = models.TextField(default=None)
    billing_details_surname = models.TextField(default=None)

    def __str__(self):
        return self.id
