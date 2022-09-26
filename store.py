from typing_extensions import Self


import product

class Store:
    products = []
    def __init__(self, name):
        self.name = name
        self.products = {}

    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    
    def sell_product(self, id):
        self.products.pop(id)
        return self
    
    #def inflation(self, percent_increase):
        


    #def set_clearance(self, category, percent_discount):
