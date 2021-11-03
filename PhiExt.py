# @ali.akgun
# @date: 03.11.2021
# @to do:
# @bugs:
# @parameters:
# @brief:
# Creates normalized external magnetic field, Phiext/Phi0

import numpy as np
INITIAL_MAGNETIC_FIELD_INTERVAL = 0
FINAL_MAGNETIC_FIELD_INTERVAL = 1

class PhiExt:
    
    def __init__ (self, magnetic_field_range, magnetic_field_resolution):
        
        self.magnetic_field_interval = magnetic_field_range
        self.magnetic_field_resolution = magnetic_field_resolution
        
    # @ali.akgun
    # @date: 03.11.2021
    # @to do:
    # @bugs:
    # @parameters:
    #   magnetic_field_range represents normalized magnetic field interval
    #   datapoints = Represents total data points of interval (Magnetic field
    #   resolution)
    # @brief:
    # Creates normalized external magnetic field, Phiext/Phi0
        
    def calculate(self, magnetic_field_range, magnetic_field_resolution):

        return np.linspace(magnetic_field_range[INITIAL_MAGNETIC_FIELD_INTERVAL],\
               magnetic_field_range[FINAL_MAGNETIC_FIELD_INTERVAL],\
               magnetic_field_resolution)