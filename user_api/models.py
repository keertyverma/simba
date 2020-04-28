from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.username
