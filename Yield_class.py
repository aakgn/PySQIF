import numpy as np
from scipy.integrate import odeint
from PhiExt import *
from Voltage import *
from Period import *



class Yield:
    
    def __init__ (self, standard_deviation, number_of_runs, parameter,\
                  magnetic_field_sample, initial_conditions, t, PhiExtArray,\
                      ib, l, ic3):
        
        self.standard_deviation = standard_deviation
        self.number_of_runs = number_of_runs
        self.parameter = parameter
        self.magnetic_field_sample = magnetic_field_sample
        self.initial_conditions = initial_conditions
        self.t = t
        self.PhiExtArray = PhiExtArray
        self.ib = ib
        self.l = l
        self.ic3 = ic3
        
        
    def calculate (self, standard_deviation, number_of_runs, parameter,\
                  magnetic_field_sample):
        
        parameter_distribution = np.random.normal(self.parameter,\
                                 self.standard_deviation, self.number_of_runs)
        voltage_margin = np.empty((self.number_of_runs,\
                                   self.magnetic_field_sample))
        
        for i in range(RUNNUM):        
            
            voltage = Voltage(initial_conditions, t, PhiExtArray, ib, l, parameter,\
                      data_points)
            voltage_margin[i, :] = voltage.calculate(initial_conditions,\
                    t, PhiExtArray, ib, l, parameter, data_points)
            


    
    
    
    
            