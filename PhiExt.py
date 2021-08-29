# @ali.akgun
# @date: 29.08.2021
# @to do:
# @bugs:
# @parameters:
# @brief:
# Creates normalized external magnetic field, Phiext/Phi0

import numpy as np

class PhiExt:
    
    def __init__ (self, initial, final, DataPoints):
        
        self.initial = initial
        self.final = final
        self.DataPoints = DataPoints
        
    # @ali.akgun
    # @date: 29.08.2021
    # @to do:
    # @bugs:
    # @parameters:
    #   initial = initial points of magnetic field interval
    #   final = final points of magnetic field interval
    #   datapoints = total data points of interval
    # @brief:
    # Creates normalized external magnetic field, Phiext/Phi0
        
    def calculate(self, initial, final, DataPoints):

        return np.linspace(initial, final, DataPoints)