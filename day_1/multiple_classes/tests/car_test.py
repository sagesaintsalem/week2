import unittest
from modules.Car import *
from modules.Engine import *
from modules.Gearbox import *


class TestCar(unittest.TestCase):
    def setUp(self):
        self.gearbox = Gearbox(5)
        self.engine = Engine(250)
        self.car = Car("black", "Focus", Engine, Gearbox)

    def test_car_colour(self):
        self.assertEqual("black", self.car.colour)

    def test_car_model(self):
        self.assertEqual("Focus", self.car.model)

    def test_car_paint_job(self):
        self.car.colour = "purple"
        self.assertEqual("purple", self.car.colour)

    def test_model_upgrade(self):
        self.car.model = "Hearse"
        self.assertEqual("Hearse", self.car.model)

    def test_engine_specs(self):
        self.assertEqual(250, self.engine.volume)

    def test_gearbox_specs(self):
        self.assertEqual(5, self.gearbox.num_of_gears)

    @unittest.skip("Wait for it")
    def test_breakdown(self):
        self.assertEqual('Danger! Car breaking down!', self.car.breakdown())

    @unittest.skip("Wait for it")
    def test_breakdown(self):
        self.assertEqual('Engine failing!', self.car.breakdown())

    @unittest.skip("Wait for it")
    def test_breakdown(self):
        self.assertEqual('Gearbox malfunction!', self.car.breakdown())

    def test_engine_failure(self):
        self.assertEqual('Engine failing!', self.engine.engine_failure())

    def test_gearbox_malfunction(self):
        self.assertEqual('Gearbox malfunction!', self.gearbox.gearbox_malfunction())