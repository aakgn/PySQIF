# @ali.akgun
# @date: 13.11.2021
# @to do:
# comments !!   
# @bugs:   
# @parameters:
# @brief: Main class

from PhiExt import *
from Voltage import *
from TimeStep import *

class InductanceConstants:
    
    def __init__ (self, l1a, l1b, l2a, l2b, l3a, l3b):
     

        self.l1a = l1a
        self.l1b = l1b
        self.l2a = l2a
        self.l2b = l2b
        self.l3a = l3a
        self.l3b = l3b

        
    # @ali.akgun
    # @date: 13.11.2021
    # @to do:
    # @bugs:
    # @parameters:
    # @brief:
        
    def calculate_l12s(self, l1a, l1b, l2a, l2b, l3a, l3b):
        
        return l1a + l1b + l2a + l2b
    
    # @ali.akgun
    # @date: 13.11.2021
    # @to do:
    # @bugs:
    # @parameters:
    # @brief:
        
    def calculate_l12d(self, l1a, l1b, l2a, l2b, l3a, l3b):
        
        return l1b - l1a + l2b - l2a
    
    # @ali.akgun
    # @date: 13.11.2021
    # @to do:
    # @bugs:
    # @parameters:
    # @brief:
        
    def calculate_l23s(self, l1a, l1b, l2a, l2b, l3a, l3b):
        
        return l2a + l2b + l3a + l3b
    
    # @ali.akgun
    # @date: 13.11.2021
    # @to do:
    # @bugs:
    # @parameters:
    # @brief:
        
    def calculate_d(self, l1a, l1b, l2a, l2b, l3a, l3b):
        
        return 3 + ((2 * self.calculate_l23s(l1a, l1b, l2a, l2b, l3a, l3b))\
                    / self.calculate_l12s(l1a, l1b, l2a, l2b, l3a, l3b)) 