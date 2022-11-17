from src.pub import Pub
from src.drink import Drink

class Customer:
    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet


    def take_from_wallet(self, amount):
        self.wallet -= amount
        

    def buy_drink(self, drink, pub):
        self.take_from_wallet(drink.price)
        pub.increase_till(drink.price)


        