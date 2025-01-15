"""
Module to implement voltage source functionality
Disclaimer: ChatGPT used for assistance in development

Filename: vsource.py
Author: Bailey Stout
Date: 2025-01-14
"""


class VSource:
    """
    Class to hold data on given VSource object. Data given in form of dictionary including "name",
    "bus1", and "v"
    """
    def __init__(self, data):
        """
        Constructor for the VSource object
        :param data: dict{"name": str, "bus1": str, "v": float}
        """
        # Error check for if data is correct type and if there are any missing keys
        if not isinstance(data, dict):
            raise TypeError("The provided data must be a dictionary.")
        required_attributes = ["name", "bus1", "v"]
        missing = [attr for attr in required_attributes if attr not in data]
        if missing:
            raise KeyError(f"Missing required attribute(s): {', '.join(missing)}")
        if not isinstance(data["name"], str):
            raise TypeError("Attribute 'name' must be of type str.")
        if not isinstance(data["bus1"], str):
            raise TypeError("Attribute 'bus1' must be of type str.")
        if not isinstance(data["v"], (float, int)):
            raise TypeError("Attribute 'v' must be of type float or int.")

        # Assign attributes
        self.name = data["name"]
        self.bus1 = data["bus1"]
        self.v = float(data["v"])

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
my_data = {
    "name": "V1",
    "bus1": "BUS1",
    "v": 5/1.01
}
vsource = VSource(my_data)
vsource.display()
'''
