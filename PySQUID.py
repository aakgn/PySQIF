# @ali.akgun
# @date: 13.11.2021
# @to do:
# Boşuna hem plot hem calculation oluşturuyorsun onu düzenle boşuna complexity !!!    
# @bugs:
# More comments !!!    
# @parameters:
# @brief: Main class

from PhiExt import *
from Voltage import *
from TimeStep import *
from InductanceConstants import *

class PySQUID:
    
    def __init__ (self, characteristic_voltage, magnetic_field_range,\
                  magnetic_field_resolution, psi_initial, ib, ic3,\
                 beta, l1a, l1b, l2a, l2b, l3a, l3b, time_resolution):
     
        self.characteristic_voltage = characteristic_voltage
        self.magnetic_field_range = magnetic_field_range
        self.magnetic_field_resolution = magnetic_field_resolution
        self.psi_initial = psi_initial
        self.ib = ib
        self.ic3 = ic3
        self.beta = beta
        self.l1a = l1a
        self.l1b = l1b
        self.l2a = l2a
        self.l2b = l2b
        self.l3a = l3a
        self.l3b = l3b
        self.time_resolution = time_resolution
        
    # @ali.akgun
    # @date: 13.11.2021
    # @to do:
    # @bugs:
    # @parameters:
    # @brief:
    
        
    def calculate(self, characteristic_voltage, magnetic_field_range,\
                  magnetic_field_resolution, psi_initial, ib, ic3, beta,\
                      l1a, l1b, l2a, l2b, l3a, l3b, time_resolution):
        
        t = TimeStep(characteristic_voltage, time_resolution)
        t = t.calculate(characteristic_voltage, time_resolution)
        PhiExtArray = PhiExt(magnetic_field_range,\
                             magnetic_field_resolution)
        PhiExtArray = PhiExtArray.calculate(magnetic_field_range,\
                             magnetic_field_resolution)
        inductance_constants = InductanceConstants(l1a, l1b, l2a, l2b, l3a, l3b)
        l12s = inductance_constants.calculate_l12s(l1a, l1b, l2a, l2b, l3a, l3b)
        l12d = inductance_constants.calculate_l12d(l1a, l1b, l2a, l2b, l3a, l3b)
        l23s = inductance_constants.calculate_l23s(l1a, l1b, l2a, l2b, l3a, l3b)
        d = inductance_constants.calculate_d(l1a, l1b, l2a, l2b, l3a, l3b)
        voltage = Voltage(psi_initial, t, PhiExtArray, ib, ic3, beta, l12s, l12d,\
                      l23s, d, magnetic_field_resolution)
        voltage.plot(psi_initial, t, PhiExtArray, ib, ic3, beta, l12s, l12d,\
                      l23s, d, magnetic_field_resolution)
        
        return voltage.calculate(psi_initial, t, PhiExtArray, ib, ic3, beta,\
                                 l12s, l12d, l23s, d, magnetic_field_resolution)
