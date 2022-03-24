# import math as m

# import numpy as np

# from math import sqrt
# import matplotlib.pyplot as plt

# print(sqrt(4))


class Product:
    def __init__(self):
        self.price = 1000

    def set_price(self, new_price):
        self.price = new_price

    def sell(self):
        print("Sold product for {}".format(self.price))


product1 = Product()
product2 = Product()
# print(product1)
# print(type(product1))
# print(product1.price)
# print(product2.price)

product1.set_price(500)
product1.sell()
product2.sell()
