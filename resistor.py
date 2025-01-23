"""
Module to implement resistor functionality
Disclaimer: ChatGPT used for assistance in development

Filename: resistor.py
Author: Bailey Stout
Date: 2025-01-14
"""


class Resistor:
    """
    Class to hold data on given Resistor object and to calculate conductance. Data given in form of
    name: str, bus1: str, bus2: str, and r: float
    """
    def __init__(self, name: str, bus1: str, bus2: str, r: float):
        """
        Constructor for the Resistor object
        :param name: Name for this Resistor object
        :param bus1: First bus connection
        :param bus2: Second bus connection
        :param r: Ohmic resistance value
        """
        # Assign attributes
        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2
        self.r = r
        self.g = self.calc_g()

    def calc_g(self):
        """
        Calculate g defined as reciprocal of r
        :return: float - internally calculated conductance
        """
        return 1/self.r

    def display(self):
        """
        Display the attributes of the Resistor object for debugging purposes
        :return:
        """
        print("Resistor Attributes:")
        print(f"\tName: {self.name}")
        print(f"\tBus 1: {self.bus1}")
        print(f"\tBus 2: {self.bus2}")
        print(f"\tResistance (R): {self.r:.4f} Ω")
        print(f"\tConductance (G): {self.g:.4f} S")


'''
# Lines for debugging
name = "R1"
bus1 = "BUS1"
bus2 = "BUS2"
r = 5.25
my_resistor = Resistor(name=name, bus1=bus1, bus2=bus2, r=r)
my_resistor.display()
'''
