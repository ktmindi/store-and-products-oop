
from product import Product

class Store:
    products = []
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    
    def sell_product(self, id):
        self.products.pop(id)
        return self
    
    #def inflation(self, percent_increase):
        


    #def set_clearance(self, category, percent_discount):
apple = Product('apple', 7, 'fruits')
store = Store('walmart') 
store.add_product(apple)
apple.update_price(.10, True)
apple.print_info()