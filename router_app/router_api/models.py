from django.db import models


# Create your models here.
class Router(models.Model):
    sapid = models.CharField(max_length=30, null=True, unique=True)
    hostname = models.CharField(max_length=100, null=True, unique=True)
    loopback = models.CharField(max_length=100, null=True, unique=True)
    mac_address = models.CharField(max_length=100, null=True, unique=True)

    class Meta:
        db_table = "router"

    def __str__(self):
        return self.sapid
