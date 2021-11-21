# @ali.akgun
# @date: 21.11.2021
# @to do:
# Boşuna hem plot hem calculation oluşturuyorsun onu düzenle boşuna complexity !!!    
# @bugs:    
# @parameters:
#    @input_file: input csv file.
# @brief: Reads input csv file and return input values as parameters.

import pandas as pd

class InputData:
    
    def __init__ (self, input_file):
     
        self.input_file = input_file
        
        
    # @ali.akgun
    # @date: 21.11.2021
    # @to do:  
    # @bugs:    
    # @parameters:
    #    @input_file: input csv file.
    # @brief: Reads input csv file and return input values as parameters.

    
        
    def initialize(self, input_file):
        
        input_data = pd.read_csv(input_file)
        psi_initial = [input_data.values[0, 1], input_data.values[1, 1]]
        magnetic_field_range = [input_data.values[2, 1], input_data.values[3, 1]]
        magnetic_field_resolution = input_data.values[4, 1]
        characteristic_voltage = input_data.values[5, 1] 
        ib = input_data.values[6, 1]
        ic3 = input_data.values[7, 1]
        time_resolution = input_data.values[8, 1]
        beta = input_data.values[9, 1]
        l1a = input_data.values[10, 1]
        l1b = input_data.values[11, 1]
        l2a = input_data.values[12, 1]
        l2b = input_data.values[13, 1]
        l3a = input_data.values[14, 1]
        l3b = input_data.values[15, 1]        
        
        return [psi_initial, magnetic_field_range, magnetic_field_resolution,\
                characteristic_voltage, ib, ic3, time_resolution, beta, l1a,
                l1b, l2a, l2b, l3a, l3b]
