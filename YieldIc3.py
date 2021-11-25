# @ali.akgun
# @date: 25.11.2021
# @to do:  
#   Yield for all simulation parameters !!!
# @bugs:
# @parameters:
# @brief:
# Generates ic3(Ic3 / Ic, Normalized current through shunt junction.)
# normal distribution according to mean and standard deviation inputs.

import numpy as np
from Voltage import *

class YieldIc3:

    # @ali.akgun
    # @date: 24.11.2021
    # @to do:  
    # @bugs:
    # @parameters:
    #   @psi_cinitial = initial conditions for solving systems of d.e. 
    #   (psi1 and psi2)
    #   @t = time step array for solving systems of differential equations.
    #   @phi_ext_array = Normalized External applied magnetic field array as 
    #   phiext/phi0
    #   @ib = Normalized bias current (Ib / Ic)
    #   ic3 = Ic3 / Ic, Normalized current through shunt junction.
    #   @l12s = l1a + l1b + l2a + l2b
    #   @l12d = l1b – l1a + l2b – l2a
    #   @l23s = l2a + l2b + l3a + l3b
    #   @d =    3 + 2l23s / l12s
    #   @magnetic_field_resolution = Represents length of external applied
    #   magnetic field array
    #   @standard_deviation = Represents standard deviation of ic3 distribution
    #   @number_of_runs = Represents length of ic3 distribution array.
    #   simulation 
    # @brief:
    # constructor method
    

    def __init__ (self, psi_initial, t, phi_ext_array, ib, ic3_mean, beta,\
                            l12s, l12d, l23s, d,\
                            magnetic_field_resolution, standard_deviation,\
                            number_of_runs):
 
        self.psi_initial = psi_initial
        self.t = t
        self.phi_ext_array = phi_ext_array
        self.ib = ib
        self.ic3_mean = ic3_mean
        self.l12s = l12s
        self.l12d = l12d
        self.l23s = l23s        
        self.d = d
        self.magnetic_field_resolution = magnetic_field_resolution
        self.standard_deviation = standard_deviation
        self.number_of_runs = number_of_runs
  
    # @ali.akgun
    # @date: 25.11.2021
    # @to do:  
    # @bugs:
    # @parameters:
    #   @psi_cinitial = initial conditions for solving systems of d.e. 
    #   (psi1 and psi2)
    #   @t = time step array for solving systems of differential equations.
    #   @phi_ext_array = Normalized External applied magnetic field array as 
    #   phiext/phi0
    #   @ib = Normalized bias current (Ib / Ic)
    #   ic3 = Ic3 / Ic, Normalized current through shunt junction.
    #   @l12s = l1a + l1b + l2a + l2b
    #   @l12d = l1b – l1a + l2b – l2a
    #   @l23s = l2a + l2b + l3a + l3b
    #   @d =    3 + 2l23s / l12s
    #   @magnetic_field_resolution = Represents length of external applied
    #   magnetic field array
    #   @standard_deviation = Represents standard deviation of ic3 distribution
    #   @number_of_runs = Represents length of ic3 distribution array.
    #   simulation 
    # @brief:
    # calculates voltage margin.

    def calculate (self, psi_initial, t, PhiExtArray, ib, ic3_mean, beta, l12s,\
                   l12d, l23s, d, magnetic_field_resolution,\
                   standard_deviation, number_of_runs):
        
        ic3 = np.random.normal(ic3_mean, standard_deviation,\
                                            number_of_runs)
        voltage_margin = np.empty((number_of_runs, magnetic_field_resolution))
        
        for i in range(number_of_runs):        
            
            voltage = Voltage(psi_initial, t, PhiExtArray, ib, ic3[i], beta,\
                                    l12s, l12d, l23s, d,\
                                    magnetic_field_resolution)
            voltage_margin[i, :] = voltage.calculate(psi_initial, t,\
                                    PhiExtArray, ib, ic3[i], beta,\
                                    l12s, l12d, l23s, d,\
                                    magnetic_field_resolution)
        return voltage_margin