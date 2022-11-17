from src.drink import Drink


class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = [Drink]

    def increase_till(self, amount):
        self.till += amount

    def sell_drink(self, customer, drink):
        customer.take_from_wallet(drink.price)
        self.increase_till(drink.price)
        