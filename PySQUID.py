# @ali.akgun
# @date: 02.11.2021
# @to do:
# Boşuna hem plot hem calculation oluşturuyorsun onu düzenle boşuna complexity !!!    
# @bugs:
# @parameters:
# @brief:

from PhiExt import *
from Voltage import *
from Period import *

class PySQUID:
    
    def __init__ (self, characteristic_voltage, magnetic_field_range,\
                  magnetic_field_resolution, psi_initial, ib, ic3,\
                 beta, l12s, l12d, l23s, d, time_resolution):
     
        self.characteristic_voltage = characteristic_voltage
        self.magnetic_field_range = magnetic_field_range
        self.magnetic_field_resolution = magnetic_field_resolution
        self.psi_initial = psi_initial
        self.ib = ib
        self.ic3 = ic3
        self.beta = beta
        self.l12s = l12s
        self.l12d = l12d
        self.l23s = l23s
        self.d = d
        self.time_resolution = time_resolution
        
    # @ali.akgun
    # @date: 01.11.2021
    # @to do:
    # @bugs:
    # @parameters:
    # @brief:
        

    
    def calculate(self, characteristic_voltage, magnetic_field_range,\
                  magnetic_field_resolution, psi_initial, ib, ic3, beta,\
                      l12s, l12d, l23s, d, time_resolution):
        
        t = Period(characteristic_voltage, time_resolution)
        t = t.calculate(characteristic_voltage, time_resolution)
        PhiExtArray = PhiExt(magnetic_field_range,\
                             magnetic_field_resolution)
        PhiExtArray = PhiExtArray.calculate(magnetic_field_range,\
                             magnetic_field_resolution)
        voltage = Voltage(psi_initial, t, PhiExtArray, ib, ic3, beta, l12s, l12d,\
                      l23s, d, magnetic_field_resolution)
        voltage.plot(psi_initial, t, PhiExtArray, ib, ic3, beta, l12s, l12d,\
                      l23s, d, magnetic_field_resolution)
        
        return voltage.calculate(psi_initial, t, PhiExt, ib, ic3, beta,\
                                 l12s, l12d, l23s, d, time_resolution)
