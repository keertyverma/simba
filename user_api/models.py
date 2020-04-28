from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255, default=None)
    password = models.CharField(max_length=255, default=None)
    shop_name = models.TextField(default=None)
    bol_client_id = models.TextField(default=None)
    bol_client_secret = models.TextField(default=None)

    def __str__(self):
        return self.name + " " + self.shop_name
