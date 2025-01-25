"""
Module to implement solution solver
Disclaimer: ChatGPT used for assistance in development

Filename: solution.py
Author: Bailey Stout
Date: 2025-01-20
"""

from circuit import Circuit


class Solution:
    """
    Class to hold data on given Solution object and perform circuit calculations. Data given in form
    of Circuit object
    """
    def __init__(self, circuit: Circuit):
        """
        Constructor for the Solution object
        :param circuit: Circuit
        """
        # Assign attributes and calculate solution
        self.circuit = circuit
        self.do_power_flow()

    def do_power_flow(self):
        """
        Use KVL to solve for series loads and resistors; assumes no parallel branches for special
        example case for this project
        :return:
        """
        # Get voltage and r_tot
        v_in = self.circuit.vsource.v
        r = []
        for resistor_name, resistor_obj in self.circuit.resistors.items():
            r.append(resistor_obj.r)
        for load_name, load_obj in self.circuit.loads.items():
            r.append(load_obj.r)
        r_tot = sum(r)

        # Calculate and set current based on voltage source and total resistance V/R = I
        current = v_in/r_tot
        self.circuit.set_i(current)

        # Go through each bus and set voltage based on resistance
        v = [v_in]  # First bus voltage will be source voltage
        for i in range(len(r)):
            remaining_r = sum(r[i + 1:])
            voltage = (remaining_r/r_tot)*v_in
            v.append(voltage)

        # Set the voltage at each bus
        counter = 0
        for bus_name, bus_obj in self.circuit.buses.items():
            bus_obj.set_bus_v(v[counter])
            counter += 1


"""
my_bus1 = "BUS1"
my_bus2 = "BUS2"

my_resistor1 = {
    "name": "R1",
    "bus1": my_bus1,
    "bus2": my_bus2,
    "r": 5
}

my_load1 = {
    "name": "L1",
    "bus1": my_bus2,
    "p": 2000,
    "v": 100
}

my_vsource1 = {
    "name": "V1",
    "bus1": my_bus1,
    "v": 100
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
"""
