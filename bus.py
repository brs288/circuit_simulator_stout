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
    def __init__(self, name=""):
        """
        Constructor for the Bus object
        :param name: str
        """
        # Error check for if name is str type
        if not isinstance(name, str):
            raise TypeError("The provided name must be of type str.")

        # Assign attributes
        self.name = name
        self.v = 0
        self.set_bus_v()

    def set_bus_v(self, v=0.):
        """
        Set bus voltage based on circuit calculations. Updates when source is created or power flow
        calculation
        :param v: float
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
