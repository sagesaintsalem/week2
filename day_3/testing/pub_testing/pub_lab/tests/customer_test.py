import unittest
from src.pub import *
from src.customer import *
from src.drink import *

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.frodo = Customer("Frodo", 17, 30)
        self.beer = Drink("Beer", 3)
        self.pub = Pub("The Prancing Pony", 100.00)
    
    def test_customer_name(self):
        self.assertEqual("Frodo", self.frodo.name)

    def test_customer_age(self):
        self.assertEqual(17, self.frodo.age)

    def test_take_from_wallet(self):
        self.frodo.take_from_wallet(5)
        self.assertEqual(25, self.frodo.wallet)

    def test_buy_drink(self):
        self.frodo.buy_drink(self.beer, self.pub)
        self.assertEqual(27, self.frodo.wallet)
        self.assertEqual(103.00, self.pub.till)

        



