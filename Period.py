# @ali.akgun
# @date: 29.08.2021
# @to do: 
#    More realistic period equation should be applied, you should check
#  a.barone book.
#  you should add more cemooents
# @bugs:
# @parameters:
# @brief:
# Creates time steps of system (tho = t*wc).

PHI0INV = 483e9 # 483GHz/mV, inverse phi0
PeriodMultiplier = 40 # You should edit this by using scientific way.
import numpy as np

class Period:
    
    def __init__ (self, characteristic_voltage, TimeDataPoints):
        
        self.characteristic_voltage = characteristic_voltage
        self.TimeDataPoints = TimeDataPoints
        
        # @ali.akgun
        # @date: 29.08.2021
        # @to do: 
        #    More realistic period equation should be applied, you should check
        # a.barone book.
        # @bugs:
        # @parameters:
        # @brief:
        # Creates time steps of system (tho = t*wc).
        
    def calculate(self, characteristic_voltage, TimeDataPoints):
        
        wc = (2 * np.pi) * PHI0INV * characteristic_voltage # 
        T = 2 * np.pi / wc
        return np.linspace(0,  T * PeriodMultiplier, TimeDataPoints) * wc