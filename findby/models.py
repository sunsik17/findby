from datetime import datetime

from django.db import models

from findby.schemas import ProductDto


# Create your models here.

class Product(models.Model):
    name: str = models.CharField(max_length=50, null=True)
    category: str = models.CharField(max_length=50, null=True)
    price: str = models.CharField(max_length=50, null=True)
    brand: str = models.CharField(max_length=50, null=True)
    link: str = models.CharField(max_length=255, null=True)
    create_date: datetime = models.DateTimeField(auto_now_add=True)
    modify_date: datetime = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def from_dto(self, dto: ProductDto):
        self.name = dto.name
        self.category = dto.category
        self.price = dto.price
        self.brand = dto.brand
        self.link = dto.link
        return self
