# @ali.akgun
# @date: 02.11.2021
# @to do:
# Boşuna hem plot hem calculation oluşturuyorsun onu düzenle boşuna complexity !!!    
# @bugs:
# @parameters:
# @brief:
# Calculates normalized voltage.

from PhiExt import *
from InputData import *
import matplotlib.pyplot as plt

class Plot:
    
    def __init__ (self, input_file, voltage):
        
        self.input_file = input_file
        self.voltage = voltage

        
    # @ali.akgun
    # @date: 29.08.2021
    # @to do:
    # @bugs:
    # @parameters:
    #   initial_conditions = initial conditions for solving systems of d.e.
    #   t = time interval of system.
    #   PhiExtArray = External magnetic field array as phiext/phi0
    #   ib = bias current
    #   l = Inductance parameter(not exactly equal to inductance !!!)
    #   ic3 = Ic3 / Ic, Normalized current through shunt junction.
    #   data_points = Total data points of normalized voltage array
    # @brief:
    # Plots meanthetadot(normalized voltage) vs 
    # normalized external magnetic field.
    
    def plot(self, input_file, voltage):
        
       input_data = InputData(input_file)
       input_data = input_data.initialize(input_file)
       magnetic_field_range = input_data[1]
       magnetic_field_resolution = int(input_data[2])
       phi_ext_array = PhiExt(magnetic_field_range,\
                             magnetic_field_resolution)
       phi_ext_array = phi_ext_array.calculate(magnetic_field_range,\
                             magnetic_field_resolution)
       plt.plot(phi_ext_array, voltage)
       plt.xlabel("PhiExternal")
       plt.ylabel("V(PhiExternal)")
       plt.title("Voltage-magnetic flux")
       plt.grid()
       plt.show()