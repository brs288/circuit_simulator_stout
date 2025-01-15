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
    dictionary including "name", "bus1", "bus2", and "r"
    """
    def __init__(self, data):
        """
        Constructor for the Resistor object
        :param data: dict{"name": str, "bus1": str, "bus2": str, "r": float}
        """
        # Error check for if data is correct type and if there are any missing keys
        if not isinstance(data, dict):
            raise TypeError("The provided data must be a dictionary.")
        required_attributes = ["name", "bus1", "bus2", "r"]
        missing = [attr for attr in required_attributes if attr not in data]
        if missing:
            raise KeyError(f"Missing required attribute(s): {', '.join(missing)}")
        if not isinstance(data["name"], str):
            raise TypeError("Attribute 'name' must be of type str.")
        if not isinstance(data["bus1"], str):
            raise TypeError("Attribute 'bus1' must be of type str.")
        if not isinstance(data["bus2"], str):
            raise TypeError("Attribute 'bus2' must be of type str.")
        if not isinstance(data["r"], (float, int)):
            raise TypeError("Attribute 'r' must be of type float or int.")

        # Assign attributes
        self.name = data["name"]
        self.bus1 = data["bus1"]
        self.bus2 = data["bus2"]
        self.r = data["r"]
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
my_data = {
    "name": "R1",
    "bus1": "BUS1",
    "bus2": "BUS2",
    "r": 5.25
}
my_resistor = Resistor(my_data)
my_resistor.display()
'''
