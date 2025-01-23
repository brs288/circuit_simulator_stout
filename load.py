"""
Module to implement load functionality
Disclaimer: ChatGPT used for assistance in development

Filename: load.py
Author: Bailey Stout
Date: 2025-01-14
"""


class Load:
    """
    Class to hold data on given Load object and to calculate conductance and power. Data given in
    form of name: str, bus1: str, v: float, and p: float
    """
    def __init__(self, name: str, bus1: str, p: float, v: float):
        """
        Constructor for the Load object
        :param name: Name for this Load object
        :param bus1: Bus connection to ground
        :param p: Rated power dissipated by load
        :param v: Rated voltage
        """
        # Assign attributes
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.v = v
        self.r = self.calc_r()
        self.g = self.calc_g()

    def calc_r(self):
        """
        Calculate r defined as v ** 2 / p
        :return: float - internally calculated resistance
        """
        return (self.v ** 2)/self.p

    def calc_g(self):
        """
        Calculate g defined as reciprocal of r
        :return: float - internally calculated conductance
        """
        return self.p/(self.v ** 2)

    def display(self):
        """Display the attributes of the Load object."""
        print("Load Attributes:")
        print(f"\tName: {self.name}")
        print(f"\tBus 1: {self.bus1}")
        print(f"\tResistance (R): {self.r:.4f} Ω")
        print(f"\tVoltage (V): {self.v:.4f} V")
        print(f"\tConductance (G): {self.g:.4f} S")
        print(f"\tPower (P): {self.p:.4f} W")


'''
# Lines for debugging
name = "L1"
bus1 = "BUS1"
p = 50
v = 230
my_load = Load(name=name, bus1=bus1, p=p, v=v)
my_load.display()
'''
