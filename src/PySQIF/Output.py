# @ali.akgun
# @date: 24.11.2021
# @to do:
# surface plot !!!  
# @bugs:
# @parameters:
# @brief:
# Plots normalized voltage response of Bi-SQUID against external applied
# magnetic field.

import pandas as pd

SINGLERUNMAGNETICFLUX = 0
SINGLERUNVOLTAGE = 1


MULTIPLERUNMAGNETICFLUX = 0
MULTIPLERUNIC3 = 1
MULTIPLERUNMRUNVOLTAGE = 2
class Output:
    
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
    
    def __init__ (self, output):
        
        self.output = output

    # @ali.akgun
    # @date: 24.11.2021
    # @to do:  
    # @bugs:
    # @parameters:
    #   @input_file = Simulation input csv file.
    # @brief:
    # Generates external normalized flux array for plotting surface/2d plots.
    
    def out_voltage(self, output):
        
        output_voltage = pd.DataFrame(output)
        output_voltage.to_csv("output_voltage.csv", index = False,\
                              header = False)
            
    def out_ic3(self, output):
        
        output_ic3 = pd.DataFrame(output)
        output_ic3.to_csv("output_ic3.csv", index = False,\
                              header = False)

    def out_normalized_magnetic_flux(self, output):
        
        normalized_magnetic_flux = pd.DataFrame(output)
        normalized_magnetic_flux.to_csv("output_normalized_magnetic_flux.csv",\
                              index = False,header = False)

    def out_single_run(self, output):
        
        self.out_voltage(output[SINGLERUNVOLTAGE])
        self.out_normalized_magnetic_flux(output[SINGLERUNMAGNETICFLUX])

    def out_multiple_run(self, output):
        
        self.out_voltage(output[MULTIPLERUNMRUNVOLTAGE])
        self.out_normalized_magnetic_flux(output[MULTIPLERUNMAGNETICFLUX])
        self.out_ic3(output[MULTIPLERUNIC3])