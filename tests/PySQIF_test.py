# @ali.akgun
# @date: 13.11.2021
# @to do:
# More test methods !!!  
# Testlere plot classının testlerini de ekle !!!  
# @bugs:
# @parameters:
# @brief:
# Test Class 

import unittest
from PySQIF import *
NEGATIVEVOLTAGE = -0.1

class MultiplicationTestCase(unittest.TestCase):
    
    
    # @ali.akgun
    # @date: 13.11.2021
    # @to do:   
    # @bugs:
    # @parameters:
    # @brief:
    # Test set-up

    def setUp(self):
        self.pysqif = PySQIF("input.csv")
            
    # @ali.akgun
    # @date: 13.11.2021
    # @to do:    
    # @bugs:
    # @parameters:
    # @brief:
    # running test !!!
    
    def test_run(self):
        result = self.pysqif.calculate("input.csv")

    # @ali.akgun
    # @date: 13.11.2021
    # @to do:    
    # @bugs:
    # @parameters:
    # @brief:
    # Negative valued voltage test.
    def test_negative_voltage(self):
        
        result = self.pysqif.calculate("input.csv")
            
        for voltage in range(len(result)):
            self.assertGreater(result[voltage], NEGATIVEVOLTAGE,\
                               "negative voltage !!!")


if __name__ == '__main__':
    unittest.main()