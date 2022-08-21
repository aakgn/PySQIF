# @ali.akgun
# @date: 21.08.2022
# @to do: random number seed case is not clear ? Is it use same seed ?!?! Test
# it with another Python file
# More test methods !!!  
# comments !!!
# @bugs:
# @parameters:
# @brief:
# This class test InductanceConstants class.

import unittest
from PySQIF.InductanceConstants import InductanceConstants as inductance_constants
import numpy as np

MINIMUM_INDUCTANCE = 0
MAXIMUM_INDUCTANCE = 100

THREE = 3
TWO = 2


class InductanceConstantsTest(unittest.TestCase):
        
            
    # @ali.akgun
    # @date: 21.08.2022
    # @to do:    
    # @bugs:
    # @parameters:
    # @brief:
    # This method tests calculate_l12s method. This method generates random 
    # numbers for l1a, l1b, l2a, l2b, l3a, l3b inductance parameters in defined
    # range. This range can be defined by using MINIMUM_INDUCTANCE
    # , and MAXIMUM_INDUCTANCE constants. After that, this method calculates
    # l12s inductance constant by using random generated inductance parameters.
    # Finally, the method compares calculated values with calculate_l12s
    # method's output. 
    # For detailed information, check InductanceConstants class.
    
    def test_calculate_l12s(self):
        
        l1a = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)
        l2a = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)
        l3a = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)
        l1b = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)
        l2b = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)
        l3b = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)            
        
        l12s = inductance_constants(l1a, l1b, l2a, l2b, l3a, l3b)
        l12s = l12s.calculate_l12s(l1a, l1b, l2a, l2b)
        
        l12s_test =  l1a + l1b + l2a + l2b
        
        self.assertAlmostEqual(l12s, l12s_test)


    # @ali.akgun
    # @date: 21.08.2022
    # @to do:    
    # @bugs:
    # @parameters:
    # @brief:
    # This method tests calculate_l12d method. This method generates random 
    # numbers for l1a, l1b, l2a, l2b, l3a, l3b inductance parameters in defined
    # range. This range can be defined by using MINIMUM_INDUCTANCE
    # , and MAXIMUM_INDUCTANCE constants. After that, this method calculates
    # l12d inductance constant by using random generated inductance parameters.
    # Finally, the method compares calculated values with calculate_l12d
    # method's output. 
    # For detailed information, check InductanceConstants class.
    
    def test_calculate_l12d(self):
        
        l1a = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)
        l2a = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)
        l3a = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)
        l1b = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)
        l2b = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)
        l3b = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)            
        
        l12d = inductance_constants(l1a, l1b, l2a, l2b, l3a, l3b)
        l12d = l12d.calculate_l12d(l1a, l1b, l2a, l2b)
        
        l12d_test =  l1b - l1a + l2b - l2a
        
        self.assertAlmostEqual(l12d, l12d_test)
        
    # @ali.akgun
    # @date: 21.08.2022
    # @to do:    
    # @bugs:
    # @parameters:
    # @brief:
    # This method tests calculate_l23s method. This method generates random 
    # numbers for l1a, l1b, l2a, l2b, l3a, l3b inductance parameters in defined
    # range. This range can be defined by using MINIMUM_INDUCTANCE
    # , and MAXIMUM_INDUCTANCE constants. After that, this method calculates
    # l23s inductance constant by using random generated inductance parameters.
    # Finally, the method compares calculated values with calculate_l23s
    # method's output. 
    # For detailed information, check InductanceConstants class.
    
    def test_calculate_l23s(self):
        
        l1a = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)
        l2a = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)
        l3a = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)
        l1b = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)
        l2b = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)
        l3b = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)            
        
        l23s = inductance_constants(l1a, l1b, l2a, l2b, l3a, l3b)
        l23s = l23s.calculate_l23s(l2a, l2b, l3a, l3b)
        
        l23s_test =  l2a + l2b + l3a + l3b
        
        self.assertAlmostEqual(l23s, l23s_test)
        
    # @ali.akgun
    # @date: 21.08.2022
    # @to do:    
    # @bugs:
    # @parameters:
    # @brief:
    # This method tests calculate_d method. This method generates random 
    # numbers for l1a, l1b, l2a, l2b, l3a, l3b inductance parameters in defined
    # range. This range can be defined by using MINIMUM_INDUCTANCE
    # , and MAXIMUM_INDUCTANCE constants. After that, this method calculates
    # d inductance constant by using random generated inductance parameters.
    # Finally, the method compares calculated values with calculate_d
    # method's output. 
    # For detailed information, check InductanceConstants class.
    
    def test_calculate_d(self):
        
        l1a = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)
        l2a = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)
        l3a = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)
        l1b = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)
        l2b = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)
        l3b = np.random.randint(MINIMUM_INDUCTANCE, MAXIMUM_INDUCTANCE)            
        
        l12s = inductance_constants(l1a, l1b, l2a, l2b, l3a, l3b)
        l12s = l12s.calculate_l12s(l1a, l1b, l2a, l2b)
        
        l23s = inductance_constants(l1a, l1b, l2a, l2b, l3a, l3b)
        l23s = l23s.calculate_l23s(l2a, l2b, l3a, l3b)
        
        
        d_test =  THREE + (TWO * l23s) / l12s
        
        d = inductance_constants(l1a, l1b, l2a, l2b, l3a, l3b)
        d = d.calculate_d(l1a, l1b, l2a, l2b, l3a, l3b)
        
        self.assertAlmostEqual(d_test, d)

if __name__ == '__main__':
    unittest.main()