from Prac_08.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel, reliability=60):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        random_chance = random.randint(0, 100)
        distance_driven = 0
        if random_chance < self.reliability:
            print("The car drives!")
            distance_driven = super().drive(distance)
            self.current_fare_distance += distance_driven
        else:
            print("The car did not drive!")
        return distance_driven
