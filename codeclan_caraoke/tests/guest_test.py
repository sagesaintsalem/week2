import unittest
from classes.guest import *
from classes.room import *


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Annie", 50)
        self.guest_2 = Guest("Bobby", 25)
        self.guest_3 = Guest("Veronica", 60)
        self.guest_4 = Guest("Tim", 80)
        self.guest_5 = Guest("Alan", 20)

    def test_names(self):
        self.assertEqual("Annie", self.guest_1.name)

    def test_wallet(self):
        self.assertEqual(60, self.guest_3.wallet)

  

