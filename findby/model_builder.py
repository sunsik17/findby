from .models import Product


class ProductBuilder:
    def __init__(self):
        self.product = Product()

    def set_name(self, name: str):
        self.product.name = name
        return self

    def set_category(self, category: str):
        self.product.category = category
        return self

    def set_price(self, price: str):
        self.product.price = price
        return self

    def set_brand(self, brand: str):
        self.product.brand = brand
        return self

    def build(self):
        return self.product