# @ali.akgun
# @date: 25.11.2021
# @to do:   
# Rakamları sayıları ifade et !!!
# @bugs:    
# @parameters:
#    @input_file: input csv file.
# @brief: Reads input csv file and return input values as parameters.

import pandas as pd

VALUES = 1
class InputData:
 
    # @ali.akgun
    # @date: 25.11.2021
    # @to do:  
    # @bugs:    
    # @parameters:
    #    @input_file: input csv file.
    # @brief: Constructor method.
    
    def __init__ (self, input_file):
     
        self.input_file = input_file
        
        
    # @ali.akgun
    # @date: 25.11.2021
    # @to do:  
    # @bugs:    
    # @parameters:
    #    @input_file: input csv file.
    # @brief: Reads input csv file and return input values as parameters.

    
        
    def initialize(self, input_file):
        
        input_data = pd.read_csv(input_file)
        psi_initial = [input_data.values[0, VALUES], input_data.values[1, VALUES]]
        magnetic_field_range = [input_data.values[2, VALUES], input_data.values[3, VALUES]]
        magnetic_field_resolution = input_data.values[4, VALUES]
        characteristic_voltage = input_data.values[5, VALUES] 
        ib = input_data.values[6, VALUES]
        ic3 = input_data.values[7, VALUES]
        time_resolution = input_data.values[8, VALUES]
        beta = input_data.values[9, VALUES]
        l1a = input_data.values[10, VALUES]
        l1b = input_data.values[11, VALUES]
        l2a = input_data.values[12, VALUES]
        l2b = input_data.values[13, VALUES]
        l3a = input_data.values[14, VALUES]
        l3b = input_data.values[15, VALUES]
        multiple_run = input_data.values[16, VALUES]         
        standard_deviation = input_data.values[17, VALUES] 
        mean = input_data.values[18, VALUES]
        number_of_runs = input_data.values[19, VALUES] 
        
        return [psi_initial, magnetic_field_range, magnetic_field_resolution,\
                characteristic_voltage, ib, ic3, time_resolution, beta, l1a,
                l1b, l2a, l2b, l3a, l3b, multiple_run, standard_deviation,\
                    mean, number_of_runs]
