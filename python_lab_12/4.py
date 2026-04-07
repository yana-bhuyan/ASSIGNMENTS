class Grandparent:
    def house(self):
        print("Grandparent's House")

class Parent(Grandparent):
    def car(self):
        print("Parent's Car")

class Child(Parent):
    def bike(self):
        print("Child's Bike")

c = Child()
c.house()
c.car()
c.bike()