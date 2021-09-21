import numpy as np
from scipy.integrate import odeint
from PhiExt import *
from Voltage import *
from Period import *



class YieldIc3:
    
    def __init__ (self, standard_deviation, number_of_runs,\
                  magnetic_field_sample, initial_conditions, t, PhiExtArray,\
                      ib, l, ic3):
        
        self.standard_deviation = standard_deviation
        self.number_of_runs = number_of_runs
        self.magnetic_field_sample = magnetic_field_sample
        self.initial_conditions = initial_conditions
        self.t = t
        self.PhiExtArray = PhiExtArray
        self.ib = ib
        self.l = l
        self.ic3 = ic3
        
        
    def calculate (self, standard_deviation, number_of_runs,\
                  magnetic_field_sample, initial_conditions, t, PhiExtArray,\
                      ib, l, ic3):
        
        ic3_distribution = np.random.normal(self.ic3,\
                                 self.standard_deviation, self.number_of_runs)
        voltage_margin = np.empty((self.number_of_runs,\
                                   self.magnetic_field_sample))
        
        for i in range(number_of_runs):        
            
            voltage = Voltage(self.initial_conditions, self.t, self.PhiExtArray,\
                              self.ib, self.l, ic3_distribution[i], 
                              self.magnetic_field_sample)
            voltage_margin[i, :] = voltage.calculate(self.initial_conditions,\
                              self.t, self.PhiExtArray, self.ib, self.l, \
                              ic3_distribution[i], self.magnetic_field_sample)
            return voltage_margin
            


    
    
    
    
            