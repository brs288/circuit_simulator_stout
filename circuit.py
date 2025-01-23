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
    Class to hold data on given Circuit object and perform circuit changes. Data given in form of
    name: str, buses: dict[str: Bus], resistors: dict[str: Resistor], loads: dict[str: Load],
    vsource: VSource"
    """
    def __init__(self, name: str, buses: dict, resistors: dict, loads: dict, vsource: VSource):
        """
        Constructor for Circuit object
        :param name: Name for this Circuit object
        :param buses: Dictionary of Bus objects
        :param resistors: Dictionary of Resistor objects
        :param loads: Dictionary of Load objects
        :param vsource: VSource object
        """
        # Assign attributes
        self.name = name
        self.buses = buses
        self.resistors = resistors
        self.loads = loads
        self.vsource = vsource
        self.i = 0.

    def add_bus(self, name: str):
        """
        Add Bus object to a Circuit object
        :param name: Name of Bus to add
        :return:
        """
        # Check if this object already exists
        if name in self.buses:
            raise ValueError(f"A bus with the name '{name}' already exists.")

        # New Bus object for Circuit object
        self.buses[name] = Bus(name=name)

    def add_resistor_element(self, name: str, bus1: str, bus2: str, r: float):
        """
        Add Resistor object to this circuit
        :param name: Name of this Resistor object
        :param bus1: First bus connection
        :param bus2: Second bus connection
        :param r: Ohmic resistance value
        :return:
        """
        # Check if this object already exists
        if name in self.resistors:
            raise ValueError(f"A resistor with the name '{name}' already exists.")

        # New Resistor object for Circuit object
        self.resistors[name] = Resistor(name=name, bus1=bus1, bus2=bus2, r=r)

    def add_load_element(self, name: str, bus1: str, p: float, v: float):
        """
        Add Load object to this circuit
        :param name: Name of Load to add
        :param bus1: Bus connection for load
        :param p: Rated power dissipation
        :param v: Rated voltage to operate
        :return:
        """
        # Check if this object already exists
        if name in self.loads:
            raise ValueError(f"A load with the name '{name}' already exists.")

        # New Load object for Circuit object
        self.loads[name] = Load(name=name, bus1=bus1, p=p, v=v)

    def add_vsource_element(self, name: str, bus1: str, v: float):
        """
        Add VSource object to this circuit
        :param name: Name for this VSource object
        :param bus1: Bus connection
        :param v: Voltage that source provides
        :return:
        """
        # This will override any existing VSource objects
        self.vsource = VSource(name=name, bus1=bus1, v=v)

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
            print(f"\tName: {current_bus}\t\tVoltage: {self.buses[current_bus].v:.4f}")

    def print_circuit_current(self):
        """
        Basic display function for circuit current
        :return:
        """
        print("Circuit Current:")
        print(f"\tCurrent: {self.i:.4f}")


"""
my_bus1 = Bus("BUS1")
my_bus2 = Bus("BUS2")

my_buses = {
    my_bus1.name: my_bus1,
    my_bus2.name: my_bus2,
}

my_resistor1 = {
    "name": "R1",
    "bus1": my_bus1.name,
    "bus2": my_bus2.name,
    "r": 200
}

my_load1 = {
    "name": "L1",
    "bus1": my_bus2.name,
    "p": 50,
    "v": 100
}

my_vsource1 = {
    "name": "V1",
    "bus1": my_bus1.name,
    "v": 200
}

new_resistor = Resistor(name=my_resistor1["name"], bus1=my_resistor1["bus1"],
                        bus2=my_resistor1["bus2"], r=my_resistor1["r"])
new_load = Load(name=my_load1["name"], bus1=my_load1["bus1"], p=my_load1["p"], v=my_load1["v"])
new_vsource = VSource(name=my_vsource1["name"], bus1=my_vsource1["bus1"], v=my_vsource1["v"])

my_circuit1 = {
    "name": "Circuit1",
    "buses": my_buses,
    "resistors": {new_resistor.name: new_resistor},
    "loads": {new_load.name: new_load},
    "vsource": new_vsource,
}

new_circuit = Circuit(name=my_circuit1["name"], buses=my_circuit1["buses"],
                      resistors=my_circuit1["resistors"], loads=my_circuit1["loads"],
                      vsource=my_circuit1["vsource"])
new_circuit.print_circuit_current()
new_circuit.print_nodal_voltage()
"""
