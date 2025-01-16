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
        :param data: dict{"name": str, "bus1": str, "p": float, "v": float}
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
        return (self.v ** 2)/self.p

    def calc_g(self):
        """Calculate conductance G as the reciprocal of resistance."""
        return 1 / self.r

    def display(self):
        """Display the attributes of the Load object."""
        print("Load Attributes:")
        print(f"  Name: {self.name}")
        print(f"  Bus 1: {self.bus1}")
        print(f"  Resistance (R): {self.r:.4f} Ω")
        print(f"  Voltage (V): {self.v:.4f} V")
        print(f"  Conductance (G): {self.g:.4f} S")
        print(f"  Power (P): {self.p:.4f} W")


# Example usage
try:
    load_data = {
        "name": "L1",
        "bus1": "A",
        "r": 50.0,
        "v": 230.0
    }
    load = Load(load_data)
    load.display()
except (KeyError, ValueError, TypeError) as e:
    print(f"Error: {e}")
