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
PSI_INITIAL_FIRST = 0
PSI_INITIAL_FINAL = 1
MAGNETIC_FIELD_RANGE_INITIAL = 2
MAGNETIC_FIELD_RANGE_FINAL = 3
MAGNETIC_FIELD_RESOLUTION = 4
CHARACTERISTIC_VOLTAGE = 5
IB = 6
IC3 = 7
TIME_RESOLUTION = 8
BETA = 9
L1A = 10
L1B = 11
L2A = 12
L2B = 13
L3A = 14
L3B = 15
MULTIPLE_RUN = 16
STANDARD_DEVIATION = 17
MEAN = 18
NUMBER_OF_RUNS = 19
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
        psi_initial = [input_data.values[PSI_INITIAL_FIRST, VALUES],\
                       input_data.values[PSI_INITIAL_FINAL, VALUES]]
        magnetic_field_range = [input_data.values[MAGNETIC_FIELD_RANGE_INITIAL,\
                                VALUES], input_data.values[MAGNETIC_FIELD_RANGE_FINAL, VALUES]]
        magnetic_field_resolution = input_data.values[MAGNETIC_FIELD_RESOLUTION,\
                                    VALUES]
        characteristic_voltage = input_data.values[CHARACTERISTIC_VOLTAGE,\
                                 VALUES] 
        ib = input_data.values[IB, VALUES]
        ic3 = input_data.values[IC3, VALUES]
        time_resolution = input_data.values[TIME_RESOLUTION, VALUES]
        beta = input_data.values[BETA, VALUES]
        l1a = input_data.values[L1A, VALUES]
        l1b = input_data.values[L1B, VALUES]
        l2a = input_data.values[L2A, VALUES]
        l2b = input_data.values[L2B, VALUES]
        l3a = input_data.values[L3A, VALUES]
        l3b = input_data.values[L3B, VALUES]
        multiple_run = input_data.values[MULTIPLE_RUN, VALUES]         
        standard_deviation = input_data.values[STANDARD_DEVIATION, VALUES] 
        mean = input_data.values[MEAN, VALUES]
        number_of_runs = input_data.values[NUMBER_OF_RUNS, VALUES] 
        
        return [psi_initial, magnetic_field_range, magnetic_field_resolution,\
                characteristic_voltage, ib, ic3, time_resolution, beta, l1a,
                l1b, l2a, l2b, l3a, l3b, multiple_run, standard_deviation,\
                    mean, number_of_runs]
