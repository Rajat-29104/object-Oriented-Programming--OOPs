# Program: Vehicle System
# Demonstrate Polymorphism and Method Overriding

class Vehicle:

    def start(self):

        print("Vehicle starts")


class Car(Vehicle):

    def start(self):

        print("Car starts with key")


class Bike(Vehicle):

    def start(self):

        print("Bike starts with self-start")


car = Car()

bike = Bike()

car.start()

bike.start()


# Sample Output

'''
Car starts with key

Bike starts with self-start
'''