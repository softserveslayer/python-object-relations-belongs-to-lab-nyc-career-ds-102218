# import car class here
from car import Car

class Person:
    def __init__(self, name, occupation):
        self._name = name
        self._occupation = occupation

    @property
    def name(self):
        return self._name

    @property
    def occupation(self):
        return self._occupation

    @classmethod
    def has_oldest_car(cls):
        cars = Car._all
        dict = {}
        for car in Car._all:
            dict[car.owner.name] = car.year
        return min(dict, key=dict.get)

    @classmethod
    def drives_a(cls, car_name):
        return [car.owner.name for car in Car._all if car.make == car_name]


    def drives_same_make_as_me(self):
        my_car = list(filter(lambda car: car.owner == self, Car._all))
        return [car.owner.name for car in Car._all if car.make == my_car[0].make and car.owner != my_car[0].owner]
