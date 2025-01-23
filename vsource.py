"""
Module to implement voltage source functionality
Disclaimer: ChatGPT used for assistance in development

Filename: vsource.py
Author: Bailey Stout
Date: 2025-01-14
"""


class VSource:
    """
    Class to hold data on given VSource object. Data given in form of name: str, bus1: str, v: float
    """
    def __init__(self, name: str, bus1: str, v: float):
        """
        Constructor for VSource object
        :param name: Name for this VSource object
        :param bus1: Bus connection
        :param v: Voltage provided by this source
        """
        # Assign attributes
        self.name = name
        self.bus1 = bus1
        self.v = v

    def display(self):
        """
        Display the attributes of the VSource object for debugging purposes
        :return:
        """
        print("Voltage Source Attributes:")
        print(f"\tName: {self.name}")
        print(f"\tBus 1: {self.bus1}")
        print(f"\tVoltage (V): {self.v:.4f} V")


'''
# Example usage
name = "V1"
bus1 = "BUS1"
v = 5/1.01
vsource = VSource(name=name, bus1=bus1, v=v)
vsource.display()
'''
