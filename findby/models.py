from datetime import datetime

from django.db import models


# Create your models here.

class Product(models.Model):
    name: str = models.CharField(max_length=50, null=True)
    category: str = models.CharField(max_length=50, null=True)
    price: str = models.BigIntegerField(default=0, null=True)
    brand: str = models.CharField(max_length=50, null=True)
    create_date: datetime = models.DateTimeField(auto_now_add=True)
    modify_date: datetime = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
