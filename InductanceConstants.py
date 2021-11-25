# @ali.akgun
# @date: 25.11.2021
# @to do:  
# @bugs:
# @parameters:
# @brief:
# Calculates Bi-SQUID normalized inductances. 
from PhiExt import *
from Voltage import *
from TimeStep import *

THREE = 3
TWO = 2

class InductanceConstants:
    
    # @ali.akgun
    # @date: 25.11.2021
    # @to do:  
    # @bugs:
    # @parameters:
    #   @l1a = l1a, and l1b represents inductances at top of circuit.
    #   (upper loop)
    #   @llb = l1a, and l1b represents inductances at top of circuit.
    #   (upper loop)
    #   @l2a = l2a, and l2b represents inductances at parallel third 
    #   Josephson Junction.
    #   @l2b = l2a, and l2b represents inductances at parallel third 
    #   Josephson Junction.
    #   @l3a = l3a, and l3b repesents inductances at bottom of circuit.
    #   @l3b = l3a, and l3b repesents inductances at bottom of circuit.
    # @brief: 
    # Constructor method
    
    def __init__ (self, l1a, l1b, l2a, l2b, l3a, l3b):
     

        self.l1a = l1a
        self.l1b = l1b
        self.l2a = l2a
        self.l2b = l2b
        self.l3a = l3a
        self.l3b = l3b

        
    # @ali.akgun
    # @date: 25.11.2021
    # @to do:  
    # @bugs:
    # @parameters:
    #   @l1a = l1a, and l1b represents inductances at top of circuit.
    #   (upper loop)
    #   @llb = l1a, and l1b represents inductances at top of circuit.
    #   (upper loop)
    #   @l2a = l2a, and l2b represents inductances at parallel third 
    #   Josephson Junction.
    #   @l2b = l2a, and l2b represents inductances at parallel third 
    #   Josephson Junction.
    # @brief: Calculates l12s
    # l12s = l1a + l1b + l2a + l2b
        
    def calculate_l12s(self, l1a, l1b, l2a, l2b):
        
        return l1a + l1b + l2a + l2b
    
    # @ali.akgun
    # @date: 25.11.2021
    # @to do:  
    # @bugs:
    # @parameters:
    #   @l1a = l1a, and l1b represents inductances at top of circuit.
    #   (upper loop)
    #   @llb = l1a, and l1b represents inductances at top of circuit.
    #   (upper loop)
    #   @l2a = l2a, and l2b represents inductances at parallel third 
    #   Josephson Junction.
    #   @l2b = l2a, and l2b represents inductances at parallel third 
    #   Josephson Junction.
    # @brief: Calculates l12d
    # l12d = l1b - l1a + l2b - l2a
        
    def calculate_l12d(self, l1a, l1b, l2a, l2b):
        
        return l1b - l1a + l2b - l2a
    
    # @ali.akgun
    # @date: 25.11.2021
    # @to do:  
    # @bugs:
    # @parameters:
    #   @l3a = l3a, and l3b repesents inductances at bottom of circuit.
    #   @l3b = l3a, and l3b repesents inductances at bottom of circuit.
    #   @l2a = l2a, and l2b represents inductances at parallel third 
    #   Josephson Junction.
    #   @l2b = l2a, and l2b represents inductances at parallel third 
    #   Josephson Junction.
    # @brief: Calculates l12d
    # l23s = l2a + l2b + l3a + l3b
        
    def calculate_l23s(self, l2a, l2b, l3a, l3b):
        
        return l2a + l2b + l3a + l3b
    
    # @ali.akgun
    # @date: 25.11.2021
    # @to do:  
    # @bugs:
    # @parameters:
    #   @l1a = l1a, and l1b represents inductances at top of circuit.
    #   (upper loop)
    #   @llb = l1a, and l1b represents inductances at top of circuit.
    #   (upper loop)
    #   @l2a = l2a, and l2b represents inductances at parallel third 
    #   Josephson Junction.
    #   @l2b = l2a, and l2b represents inductances at parallel third 
    #   Josephson Junction.
    #   @l3a = l3a, and l3b repesents inductances at bottom of circuit.
    #   @l3b = l3a, and l3b repesents inductances at bottom of circuit.
    # @brief: Calculates d
    # d =    3 + 2l23s / l12s
        
    def calculate_d(self, l1a, l1b, l2a, l2b, l3a, l3b):
        
        return THREE + ((TWO * self.calculate_l23s(l2a, l2b, l3a, l3b))\
                    / self.calculate_l12s(l1a, l1b, l2a, l2b)) 