# @ali.akgun
# @date: 24.11.2021
# @to do:
# surface plot !!!  
# @bugs:
# @parameters:
# @brief:
# Plots normalized voltage response of Bi-SQUID against external applied
# magnetic field.

from PhiExt import *
from InputData import *
import matplotlib.pyplot as plt

class Plot:
    
    # @ali.akgun
    # @date: 24.11.2021
    # @to do:  
    # @bugs:
    # @parameters:
    #   @voltage = normalized voltage response of Bi-SQUID against 
    #   external applied magnetic field.
    #   @input_file = Simulation input csv file.
    # @brief:
    # constructor method
    
    def __init__ (self, voltage, input_file):
        
        self.input_file = input_file
        self.voltage = voltage
 
    # @ali.akgun
    # @date: 24.11.2021
    # @to do:  
    # @bugs:
    # @parameters:
    #   @voltage = normalized voltage response of Bi-SQUID against 
    #   external applied magnetic field.
    #   @input_file = Simulation input csv file.
    # @brief:
    # Plots normalized voltage response of Bi-SQUID against external applied
    # magnetic field.
    
    def plot(self, voltage, input_file):
        
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