# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle():  # base class
    def __init__(self, v):
        self.v = v


class FlightVehicle(Vehicle):
    def __init__(self, v, fv):
        super().__init__(v)
        self.fv = fv


class Starship(FlightVehicle):
    def __init__(self, v, fv, s):
        super().__init__(v, fv)
        self.s = s


class Airplane(FlightVehicle):
    def __init__(self, v, fv, a):
        super().__init__(v, fv)
        self.a = a


class GroundVehicle(Vehicle):
    def __init__(self, v, gv):
        super().__init__(v)
        self.gv = gv


class Car(GroundVehicle):
    def __init__(self, v, gv, c):
        super().__init__(v, gv)
        self.c = c


class Motorcycle(GroundVehicle):
    def __init__(self, v, gv, m):
        super().__init__(v, gv)
        self.m = m
