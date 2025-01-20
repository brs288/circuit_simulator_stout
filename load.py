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
    form of dictionary including "name", "bus1", "v", and "p"
    """
    def __init__(self, data):
        """
        Constructor for the Load object
        :param data: Dict["name": str, "bus1": str, "p": float, "v": float]
        """
        # Error check for if data is correct type and if there are any missing keys
        if not isinstance(data, dict):
            raise TypeError("The provided data must be a dictionary.")
        required_attributes = ["name", "bus1", "p", "v"]
        missing = [attr for attr in required_attributes if attr not in data]
        if missing:
            raise KeyError(f"Missing required attribute(s): {', '.join(missing)}")
        if not isinstance(data["name"], str):
            raise TypeError("Attribute 'name' must be of type str.")
        if not isinstance(data["bus1"], str):
            raise TypeError("Attribute 'bus1' must be of type str.")
        if not isinstance(data["p"], (float, int)):
            raise TypeError("Attribute 'p' must be of type float or int.")
        if not isinstance(data["v"], (float, int)):
            raise TypeError("Attribute 'v' must be of type float or int.")

        # Assign attributes
        self.name = data["name"]
        self.bus1 = data["bus1"]
        self.p = float(data["p"])
        self.v = float(data["v"])
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
        return 1 / self.r

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
my_data = {
    "name": "L1",
    "bus1": "BUS1",
    "p": 50.,
    "v": 230.
}
my_load = Load(my_data)
my_load.display()
'''
