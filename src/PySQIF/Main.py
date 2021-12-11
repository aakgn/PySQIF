# @ali.akgun
# @date: 25.11.2021
# @to do:
# Inputları almak için daha uygun bir yapı oluştur !!! 
# Simplify communiciation between other classes !!!   
# @bugs:
# @parameters:
# @brief:
# Main Class

try:
    # When running from pip installation
    from .PhiExt import *
    from .Voltage import *
    from .TimeStep import *
    from .InductanceConstants import *
    from .InputData import *
    from .YieldIc3 import *
    from .Output import *
except ImportError:
    # When running from source without pip installation
    from PhiExt import *
    from Voltage import *
    from TimeStep import *
    from InductanceConstants import *
    from InputData import *
    from YieldIc3 import *
    from Output import *


class Main:
    
    # @ali.akgun
    # @date: 25.11.2021
    # @to do:  
    # @bugs:
    # @parameters:
    #   @input_file = input csv file for simulation.
    # @brief:
    # constructor method
    def __init__ (self, input_file):
     
        self.input_file = input_file
   
    # @ali.akgun
    # @date: 25.11.2021
    # @to do:  
    # @bugs:
    # @parameters:
    #   @input_file = input csv file for simulation.
    # @brief:
    # protocol bertween classes
    
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
        multiple_run = input_data[14]         
        standard_deviation = input_data[15] 
        mean = input_data[16]
        number_of_runs = int(input_data[17])
        
        inductance_constants = InductanceConstants(l1a, l1b, l2a, l2b, l3a, l3b)
        l12s = inductance_constants.calculate_l12s(l1a, l1b, l2a, l2b)
        l12d = inductance_constants.calculate_l12d(l1a, l1b, l2a, l2b)
        l23s = inductance_constants.calculate_l23s(l2a, l2b, l3a, l3b)
        d = inductance_constants.calculate_d(l1a, l1b, l2a, l2b, l3a, l3b)
        t = TimeStep(characteristic_voltage, time_resolution)
        t = t.calculate(characteristic_voltage, time_resolution)
        phi_ext_array = PhiExt(magnetic_field_range,\
                             magnetic_field_resolution)
        phi_ext_array = phi_ext_array.calculate(magnetic_field_range,\
                             magnetic_field_resolution)
        voltage = Voltage(psi_initial, t, phi_ext_array, ib, ic3, beta, l12s, l12d,\
                      l23s, d, magnetic_field_resolution)
        
        
        if (multiple_run == 1):
            
            output = YieldIc3(psi_initial, t, phi_ext_array, ib, mean, beta,\
                               l12s, l12d, l23s, d,\
                               magnetic_field_resolution, standard_deviation,\
                               number_of_runs)
            output = output.calculate(psi_initial, t, phi_ext_array, ib, mean, beta,\
                                  l12s, l12d, l23s, d,\
                                  magnetic_field_resolution, standard_deviation,\
                                  number_of_runs)
            output_file = Output(output)
            output_file = output_file.out_multiple_run(output)
            return output
            
        
        voltage = voltage.calculate(psi_initial, t, phi_ext_array, ib, ic3, beta,\
                                 l12s, l12d, l23s, d, magnetic_field_resolution)
        output = [phi_ext_array, voltage]
        
        output_file = Output(output)
        output_file = output_file.out_single_run(output)
        
        return output
