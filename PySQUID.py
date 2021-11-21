# @ali.akgun
# @date: 13.11.2021
# @to do:
# Boşuna hem plot hem calculation oluşturuyorsun onu düzenle boşuna complexity !!!
# Inputları almak için daha uygun bir yapı oluştur !!!    
# @bugs:
# More comments !!!    
# @parameters:
# @brief: Main class

from PhiExt import *
from Voltage import *
from TimeStep import *
from InductanceConstants import *
from InputData import *

class PySQUID:
    
    def __init__ (self, input_file):
     
        self.input_file = input_file

        
    # @ali.akgun
    # @date: 13.11.2021
    # @to do:
    # @bugs:
    # @parameters:
    # @brief:
    
        
    def calculate(self, input_file):
        
        
        input_data = InputData(input_file)
        input_data = input_data.initialize(input_file)
        psi_initial = input_data[0]
        magnetic_field_range = input_data[1]
        magnetic_field_resolution = int(input_data[2])
        characteristic_voltage = input_data[3] 
        ib = input_data[4]
        ic3 = input_data[5]
        time_resolution = int(input_data[6])
        beta = input_data[7]
        l1a = input_data[8]
        l1b = input_data[9]
        l2a = input_data[10]
        l2b = input_data[11]
        l3a = input_data[12]
        l3b = input_data[13]   
        
        
        inductance_constants = InductanceConstants(l1a, l1b, l2a, l2b, l3a, l3b)
        l12s = inductance_constants.calculate_l12s(l1a, l1b, l2a, l2b, l3a, l3b)
        l12d = inductance_constants.calculate_l12d(l1a, l1b, l2a, l2b, l3a, l3b)
        l23s = inductance_constants.calculate_l23s(l1a, l1b, l2a, l2b, l3a, l3b)
        d = inductance_constants.calculate_d(l1a, l1b, l2a, l2b, l3a, l3b)
        t = TimeStep(characteristic_voltage, time_resolution)
        t = t.calculate(characteristic_voltage, time_resolution)
        PhiExtArray = PhiExt(magnetic_field_range,\
                             magnetic_field_resolution)
        PhiExtArray = PhiExtArray.calculate(magnetic_field_range,\
                             magnetic_field_resolution)
        voltage = Voltage(psi_initial, t, PhiExtArray, ib, ic3, beta, l12s, l12d,\
                      l23s, d, magnetic_field_resolution)
            
        return voltage.calculate(psi_initial, t, PhiExtArray, ib, ic3, beta,\
                                 l12s, l12d, l23s, d, magnetic_field_resolution)
