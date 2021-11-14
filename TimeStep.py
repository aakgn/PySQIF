# @author: ali.akgun
# @date: 02.11.2021
# @to do: 
#  More realistic period equation should be applied, you should check
#  a.barone book.
#  you should add more cemooents
# @bugs:
# @parameters:
#  characteristic_voltage of Josephson Junction (IcRn)
#  time_resolution    
# @brief:
# Creates time steps of system (tho = t*wc).
# Time steps defined for solving Josephson Junction based differential equation
# system. 
# We should analyze the system
# by using infinite-like period for getting realistic result against DC bias
# voltage. Thus, we defined PeriodMultiplier parameter, this parameter controls
# length of the time step period. 
# wc = (2 * pi / Phi_0) * Vc, Vc = Ic * Rn
# @references: 
# (i) The SQUID handbook, josephson junction section. (Definition of
# characteristic frequency)
# (ii) Bi-SQUID: a novel linearization method for dc SQUID voltage response


PHI0INV = 483e9 # 483GHz/mV, inverse phi0
PeriodMultiplier = 100 # You should edit this by using scientific way.
import numpy as np

class TimeStep:
    
        # @ali.akgun
        # @date: 02.11.2021
        # @to do: 
        # @bugs:
        # @parameters:
        # @brief: Constructor method
        
    def __init__ (self, characteristic_voltage, time_resolution):
        
        self.characteristic_voltage = characteristic_voltage
        self.time_resolution = time_resolution
        
        # @ali.akgun
        # @date: 29.08.2021
        # @to do: 
        #    More realistic period equation should be applied, you should check
        # a.barone book.
        # @bugs:
        # @parameters:
        # @brief:
        # Creates time steps of system (tho = t*wc).
        
    def calculate(self, characteristic_voltage, time_resolution):
        
        wc = (2 * np.pi) * PHI0INV * characteristic_voltage # 
        T = 2 * np.pi / wc
        return np.linspace(0,  T * PeriodMultiplier, time_resolution) * wc