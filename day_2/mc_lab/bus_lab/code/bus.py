from code.bus_stop import BusStop
class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, passenger_1):
        return self.passengers.append(passenger_1)

    def drop_off(self, passenger_2):
        return self.passengers.remove(passenger_2)

    def empty(self):
        return self.passengers.clear()

    def pick_up_from_stop(self, bus_stop: BusStop):
        self.passengers.extend(bus_stop.queue)
        bus_stop.queue.clear()

    def drive(self):
        return "Brum brum"