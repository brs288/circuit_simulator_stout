"""
Main script to run circuit simulation
Disclaimer: ChatGPT used for assistance in development

Filename: main.py
Author: Bailey Stout
Date: 2025-01-22
"""

from solution import Solution
from circuit import Circuit

# --- EDIT PARAMETERS HERE --- #

# Resistance to use between buses
r = 5

# KVL calculations compatible with one load object
p = 2000
v = 100

# Voltage source rating
v_in = 100

# Bus names
first_bus = "BUS1"
second_bus = "BUS2"

# ---------------------------- #

my_bus1 = "BUS1"
my_bus2 = "BUS2"

my_resistor1 = {
    "name": "R1",
    "bus1": my_bus1,
    "bus2": my_bus2,
    "r": r
}

my_load1 = {
    "name": "L1",
    "bus1": my_bus2,
    "p": p,
    "v": v
}

my_vsource1 = {
    "name": "V1",
    "bus1": my_bus1,
    "v": v_in
}

new_circuit = Circuit(name="Circuit1")
new_circuit.add_bus(name=my_bus1)
new_circuit.add_bus(name=my_bus2)
new_circuit.add_resistor_element(name=my_resistor1["name"], bus1=my_resistor1["bus1"],
                                 bus2=my_resistor1["bus2"], r=my_resistor1["r"])
new_circuit.add_load_element(name=my_load1["name"], bus1=my_load1["bus1"], p=my_load1["p"],
                             v=my_load1["v"])
new_circuit.add_vsource_element(name=my_vsource1["name"], bus1=my_vsource1["bus1"],
                                v=my_vsource1["v"])

new_solution = Solution(new_circuit)
new_solution.circuit.print_circuit_current()
new_solution.circuit.print_nodal_voltage()
