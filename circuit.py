"""
Module to implement circuit functionality
Disclaimer: ChatGPT used for assistance in development

Filename: circuit.py
Author: Bailey Stout
Date: 2025-01-16
"""

from bus import Bus
from resistor import Resistor
from load import Load
from vsource import VSource


class Circuit:
    """
    Class to hold data on given Circuit object and perform circuit calculations. Data given in form
    of dictionary including "name", "buses", "resistors", "loads", and "vsource"
    """
    def __init__(self, data):
        """
        Constructor for the Circuit object
        :param data: Dict["name": str, "buses": Dict[str, Bus], "resistors": Dict[str, Resistor],
        "loads": Dict[str, Load], "vsource": VSource]
        """
        # Error check for if data is correct type and if there are any missing keys
        if not isinstance(data, dict):
            raise TypeError("The provided data must be a dictionary.")
        required_attributes = ["name", "buses", "resistors", "loads", "vsource"]
        missing = [attr for attr in required_attributes if attr not in data]
        if missing:
            raise KeyError(f"Missing required attribute(s): {', '.join(missing)}")

        if not isinstance(data["name"], str):
            raise TypeError("Attribute 'name' must be of type str.")

        if not isinstance(data["buses"], dict):
            raise TypeError("Attribute 'buses' must be of type Dict[str, Bus].")
        for key, value in data["buses"].items():
            if not isinstance(key, str):
                raise TypeError("Keys in 'buses' must be of type str.")
            if not isinstance(value, Bus):
                raise TypeError("Values in 'buses' must be instances of class Bus.")

        if not isinstance(data["resistors"], dict):
            raise TypeError("Attribute 'resistors' must be of type Dict[str, Resistor].")
        for key, value in data["resistors"].items():
            if not isinstance(key, str):
                raise TypeError("Keys in 'resistors' must be of type str.")
            if not isinstance(value, Resistor):
                raise TypeError("Values in 'resistors' must be instances of class Resistor.")

        if not isinstance(data["loads"], dict):
            raise TypeError("Attribute 'loads' must be of type Dict[str, Load].")
        for key, value in data["loads"].items():
            if not isinstance(key, str):
                raise TypeError("Keys in 'loads' must be of type str.")
            if not isinstance(value, Load):
                raise TypeError("Values in 'loads' must be instances of class Load.")

        if not isinstance(data["vsource"], VSource):
            raise TypeError("Attribute 'vsource' must be of type VSource.")

        # Assign attributes
        self.name = data["name"]
        self.buses = data["buses"]
        self.resistors = data["resistors"]
        self.loads = data["loads"]
        self.vsource = data["vsource"]
        self.i = 0
        self.set_i()

    def add_bus(self, name=""):
        """
        Add Bus object to a Circuit object
        :param name: str
        :return:
        """
        # Check if this key already exists
        if name in self.buses:
            raise ValueError(f"A bus with the name '{name}' already exists.")

        # New Bus object for Circuit object
        self.buses[name] = Bus(name=name)

    def add_resistor_element(self, data):
        """
        Add Resistor object to a Circuit object
        :param data: Dict["name": str, "bus1": str, "bus2": str, "r": float]
        :return:
        """
        # Check if this key already exists
        if data["name"] in self.resistors:
            raise ValueError(f"A resistor with the name '{data['name']}' already exists.")

        # New Resistor object for Circuit object
        self.resistors[data["name"]] = Resistor(data)

    def add_load_element(self, data):
        """
        Add Load object to a Circuit object
        :param data: Dict["name": str, "bus1": str, "p": float, "v": float]
        :return:
        """
        # Check if this key already exists
        if data["name"] in self.loads:
            raise ValueError(f"A load with the name '{data['name']}' already exists.")

        # New Load object for Circuit object
        self.loads[data["name"]] = Load(data)

    def add_vsource_element(self, data):
        """
        Add VSource object to a Circuit object
        :param data: Dict["name": str, "bus1": str, "v": float]
        :return:
        """
        # This will override any existing VSource objects
        self.vsource = VSource(data)

    def set_i(self, i=0.):
        """
        Set function for current
        :param i: float
        :return:
        """
        self.i = i

    def print_nodal_voltage(self):
        """
        Basic display function for each bus voltage
        :return:
        """
        print("Bus Voltages Attributes:")
        for current_bus in self.buses:
            print(f"\tName: {current_bus}\t\tVoltage: {self.buses[current_bus].v}")

    def print_circuit_current(self):
        """
        Basic display function for circuit current
        :return:
        """
        print("Circuit Current:")
        print(f"\tCurrent: {self.i:.4f}")

'''
my_bus1 = Bus("BUS1")
my_bus2 = Bus("BUS2")
my_bus3 = Bus("BUS3")

my_buses = {
    my_bus1.name: my_bus1,
    my_bus2.name: my_bus2,
}

my_resistor1 = {
    "name": "R1",
    "bus1": my_bus1.name,
    "bus2": my_bus2.name,
    "r": 5.25
}

my_resistor2 = {
    "name": "R2",
    "bus1": my_bus2.name,
    "bus2": my_bus3.name,
    "r": 15
}

my_load1 = {
    "name": "L1",
    "bus1": my_bus2.name,
    "p": 50.,
    "v": 100.
}

my_load2 = {
    "name": "L2",
    "bus1": my_bus3.name,
    "p": 250,
    "v": 101
}

my_vsource1 = {
    "name": "V1",
    "bus1": my_bus1.name,
    "v": 240 / 2
}

my_vsource2 = {
    "name": "V2",
    "bus1": my_bus1.name,
    "v": 241.1 / 2.01
}

new_resistor = Resistor(my_resistor1)
new_load = Load(my_load1)
new_vsource = VSource(my_vsource1)

my_circuit1 = {
    "name": "Circuit1",
    "buses": my_buses,
    "resistors": {new_resistor.name: new_resistor},
    "loads": {new_load.name: new_load},
    "vsource": new_vsource,
}

new_circuit = Circuit(my_circuit1)
new_circuit.print_circuit_current()
new_circuit.print_nodal_voltage()
print("\n\n")
new_circuit.add_bus("BUS3")
new_circuit.add_resistor_element(my_resistor2)
new_circuit.add_load_element(my_load2)
new_circuit.add_vsource_element(my_vsource2)
new_circuit.print_circuit_current()
new_circuit.print_nodal_voltage()
'''
