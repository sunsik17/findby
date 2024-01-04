from datetime import datetime

from django.db import models


# Create your models here.

class Product(models.Model):
    name: str = models.CharField(max_length=50)
    category: str = models.CharField(max_length=50)
    price: str = models.BigIntegerField(default=0)
    create_date: datetime = models.DateTimeField(auto_now_add=True)
    modify_date: datetime = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
