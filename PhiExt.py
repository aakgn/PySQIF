# @ali.akgun
# @date: 25.11.2021
# @to do:
# @bugs:
# @parameters:
# @brief:
# Creates normalized external magnetic field, Phiext/Phi0

import numpy as np
INITIAL_MAGNETIC_FIELD_INTERVAL = 0
FINAL_MAGNETIC_FIELD_INTERVAL = 1

class PhiExt:
    
    # @ali.akgun
    # @date: 25.11.2021
    # @to do:  
    # @bugs:
    # @parameters:
    #   @magnetic_field_range = Represents range of external applied
    #   magnetic field array
    #   @magnetic_field_resolution = Represents length of external applied
    #   magnetic field array(interval of array)
    # @brief:
    # constructor method
    
    def __init__ (self, magnetic_field_range, magnetic_field_resolution):
        
        self.magnetic_field_interval = magnetic_field_range
        self.magnetic_field_resolution = magnetic_field_resolution
         
    # @ali.akgun
    # @date: 25.11.2021
    # @to do:  
    # @bugs:
    # @parameters:
    #   @magnetic_field_range = Represents range of external applied
    #   magnetic field array(interval of array)
    #   @magnetic_field_resolution = Represents length of external applied
    #   magnetic field array(Represents total data points of interval)
    # @brief:
    # Creates normalized external magnetic field, Phiext/Phi0
        
    def calculate(self, magnetic_field_range, magnetic_field_resolution):

        return np.linspace(magnetic_field_range[INITIAL_MAGNETIC_FIELD_INTERVAL],\
               magnetic_field_range[FINAL_MAGNETIC_FIELD_INTERVAL],\
               magnetic_field_resolution)