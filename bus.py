"""
Module to implement bus functionality
Disclaimer: ChatGPT used for assistance in development

Filename: bus.py
Author: Bailey Stout
Date: 2025-01-14
"""


class Bus:
    """
    Class to hold data on given Bus object and to calculate conductance. Data given in form of
    string used as a name
    """
    def __init__(self, name: str):
        """
        Constructor for the Bus object
        :param name: Name for the Bus object
        """
        # Assign attributes
        self.name = name
        self.v = float
        self.set_bus_v(0.)

    def set_bus_v(self, v: float):
        """
        Set bus voltage based on circuit calculations. Updates when source is created or power flow
        calculation
        :param v: Voltage at this bus
        :return:
        """
        self.v = v

    def display(self):
        """
        Display the attributes of the Bus object for debugging purposes
        :return:
        """
        print("Bus Attributes:")
        print(f"\tName: {self.name}")
        print(f"\tVoltage: {self.v:.4f}")


'''
# Lines for debugging
name = "BUS1"
my_bus = Bus(name)
my_bus.display()
my_bus.set_bus_v(50/49)
my_bus.display()
'''
