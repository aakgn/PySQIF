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
                  magnetic_field_resolution, initial_conditions, ib, l, ic3,\
                  time_resolution):
     
        self.characteristic_voltage = characteristic_voltage
        self.magnetic_field_range = magnetic_field_range
        self.magnetic_field_resolution = magnetic_field_resolution
        self.initial_conditions = initial_conditions
        self.ib = ib
        self.l = l
        self.ic3 = ic3
        self.time_resolution = time_resolution
        
    # @ali.akgun
    # @date: 01.11.2021
    # @to do:
    # @bugs:
    # @parameters:
    # @brief:
        

    
    def calculate(self, characteristic_voltage, magnetic_field_range,\
                  magnetic_field_resolution, initial_conditions, ib, l, ic3,\
                  time_resolution):
        
        t = Period(characteristic_voltage, time_resolution)
        t = t.calculate(characteristic_voltage, time_resolution)
        PhiExtArray = PhiExt(magnetic_field_range,\
                             magnetic_field_resolution)
        PhiExtArray = PhiExtArray.calculate(magnetic_field_range,\
                             magnetic_field_resolution)
        voltage = Voltage(initial_conditions, t, PhiExtArray,\
                          ib, l, ic3, time_resolution)
        voltage.plot(initial_conditions, t, PhiExtArray,\
                          ib, l, ic3, magnetic_field_resolution)
        
        return voltage.calculate(initial_conditions, t,\
                                 PhiExtArray, ib, l, ic3,\
                                 magnetic_field_resolution)
