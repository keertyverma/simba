"""
Models created to handle seller and shipments data
"""

from django.db import models
from django.contrib.auth.models import AbstractUser


class Shipment(models.Model):
    shipment_id = models.IntegerField(primary_key=True, default=None)
    shop_client_id = models.CharField(max_length=50, default=None)
    fulfilment_method = models.CharField(max_length=15, default=None)
    shipment_date = models.TextField(default=None)
    shipment_reference = models.TextField(default=None, null=True)
    pick_up_point = models.BooleanField(default=None)
    zip_code = models.TextField(default=None)
    country_code = models.TextField(default=None)

    def __str__(self):
        return self.shop_client_id


class ShipmentDataRefresh(models.Model):
    username = models.CharField(
        max_length=50, blank=True, null=True, default=None)
    shop_client_id = models.TextField(
        blank=True, null=True, default=None, max_length=96)
    update_time = models.DateTimeField(
        auto_now_add=True, null=True)

    def __str__(self):
        return self.bol_client_id


class Seller(AbstractUser):
    shop_name = models.TextField(
        blank=True, null=True, default=None, max_length=96)
    bol_client_id = models.TextField(
        blank=True, null=True, default=None, max_length=96)
    bol_client_secret = models.TextField(
        blank=True, null=True, default=None, max_length=96)

    def __str__(self):
        return self.email
