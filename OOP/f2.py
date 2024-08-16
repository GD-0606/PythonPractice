"""
    Data Encapuslation adn Data Abstraction in python

    Data Encapsulation meaning that combining the data members and methods that works on that data under single unit like a class.
    it hide the internal details of an object from outside, by making some parts private.
"""

class Car:
    def __init__(self,make,type,year):
        self.make=make
        self._type=type
        self.__year=year
    def get_year(self):
        print(f"year is {self.__year}")
    # private method
    def __get(self):
        print(self.make)


car = Car("Toyota", "Corolla", 2020)
car.get_year()