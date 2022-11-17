import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self): # NEW
      self.pub = Pub("The Prancing Pony", 100.00)
      


    def test_pub_has_name(self): # NEW
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_till(self):
        self.pub.increase_till(20.00)
        self.assertEqual(120.00, self.pub.till)

    @unittest.skip("Extension")
    def test_id_age(self):
        self.assertEqual("Refused service", self.id_age(Customer.customer.age))