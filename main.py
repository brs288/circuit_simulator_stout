"""
Main script to run circuit simulation
Disclaimer: ChatGPT used for assistance in development

Filename: main.py
Author: Bailey Stout
Date: 2025-01-22
"""

from solution import Solution
from circuit import Circuit
from bus import Bus
from resistor import Resistor
from load import Load
from vsource import VSource

# --- EDIT PARAMETERS HERE --- #

# Resistance to use between buses
r = 5

# KVL calculations compatible with one load object
p = 2000
v = 100

# Voltage source rating
v_in = 100

# Bus names
first_bus = "bus A"
second_bus = "bus B"

# ---------------------------- #

my_bus1 = Bus(first_bus)
my_bus2 = Bus(second_bus)

my_buses = {
    my_bus1.name: my_bus1,
    my_bus2.name: my_bus2,
}

my_resistor1 = {
    "name": "R1",
    "bus1": my_bus1.name,
    "bus2": my_bus2.name,
    "r": r
}

my_load1 = {
    "name": "L1",
    "bus1": my_bus2.name,
    "p": p,
    "v": v
}

my_vsource1 = {
    "name": "V1",
    "bus1": my_bus1.name,
    "v": v_in
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

new_solution = Solution(new_circuit)
new_solution.circuit.print_circuit_current()
new_solution.circuit.print_nodal_voltage()
