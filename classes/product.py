from cgi import print_exception
from tokenize import ContStr


class Product:
    products = []
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        Product.products.append(self)
    
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price +=(self.price * percent_change)
        else:
            self.price -=(self.price * percent_change)
        return self

    
    def print_info(self):
        print(f"Product Name: {self.name} Product Category: {self.category} Price: $ {self.price}")



product_one = Product("banana", 3, "produce")
product_two = Product("lettuce", 2, "produce")

Product.print_info(product_one)
