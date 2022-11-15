import unittest
from code.bus import Bus
from code.bus_stop import BusStop
from code.person import Person

class TestBus(unittest.TestCase):
    def setUp(self):
        self.bus = Bus(22, "Ocean Terminal")


    def test_has_route_number(self):
        self.assertEqual(22, self.bus.route_number)



    def test_has_destination(self):
        self.assertEqual("Ocean Terminal", self.bus.destination)



    def test_can_drive(self):
        self.assertEqual("Brum brum", self.bus.drive())


    def test_starts_with_no_passengers(self):
        self.assertEqual(0, self.bus.passenger_count())


    def test_can_pick_up_passenger(self):
        person = Person("Guido van Rossum", 64)
        self.bus.pick_up(person)
        self.assertEqual(1, self.bus.passenger_count())


    def test_can_drop_off_passenger(self):
        person = Person("Guido van Rossum", 64)
        self.bus.pick_up(person)
        self.bus.drop_off(person)
        self.assertEqual(0, self.bus.passenger_count())


    def test_can_empty_bus(self):
        person = Person("Guido van Rossum", 64)
        self.bus.pick_up(person)
        self.bus.empty()
        self.assertEqual(0, self.bus.passenger_count())


    def test_can_pick_up_passenger_from_bus_stop(self):
        person_1 = Person("Guido van Rossum", 64)
        person_2 = Person("Carol Willing", 50)
        bus_stop = BusStop("Waverley Station")
        bus_stop.add_to_queue(person_1)
        bus_stop.add_to_queue(person_2)
        self.bus.pick_up_from_stop(bus_stop)
        self.assertEqual(2, self.bus.passenger_count())
