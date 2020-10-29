from dataclasses import dataclass
from buying.errors import ProductNotFound
from buying.data import get_data

@dataclass
class ProductModel():
    id: int
    name: str
    price: int
    amount: int

class Product():
    def __init__(self):
        self.products = []
        for i in get_data():
            self.products.append(ProductModel(**i))
            # self.products.append(ProductModel(i['id'], i['name'], i['price'], i['amount']))

    def get_all(self):
        return self.products

    def get(self, id):
        if type(id) != int:
            raise ValueError("id is not integer")
        for i in self.products:
            if i.id == id:
                return i
        raise ProductNotFound("product id is wrong")

    def buy(self, id, quantity):
        for i in self.products:
            if i.id == id:
                i.amount -= quantity