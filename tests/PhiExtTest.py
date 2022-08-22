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
from PySQIF.PhiExt import PhiExt as phiext
import numpy as np

MINIMUM_MAGNETIC_FLUX = 0
MAXIMUM_MAGNETIC_FLUX = 1000

MINIMUM_MAGNETIC_FILED_RESOLUTION = 0
MAXIMUM_MAGNETIC_FILED_RESOLUTION = 1000

FIRST_ELEMENT = 0
LAST_ELEMENT = -1

class TimeStepTest(unittest.TestCase):
        
            
    # @ali.akgun
    # @date: 21.08.2022
    # @to do:    
    # @bugs:
    # @parameters:
    # @brief:
    # This method tests calculate method in PhiEXT class. This method fills 
    # external normalized magnetic flux array in randomly defined 
    # range. This range can be defined by using MINIMUM_MAGNETIC_FLUX
    # , and MAXIMUM_MAGNETIC_FLUX constants. Resolution of the array is also
    # defined by randum numbers. This random number is generated between 
    # MINIMUM_MAGNETIC_FILED_RESOLUTION, and MAXIMUM_MAGNETIC_FILED_RESOLUTION.
    # After that, this method generates normalized magnetic flux array by using
    # randomly defined range and resolution.
    # Finally, the method compares randomly generated normalized magnetic flux
    # array with calculate method output from PhiExt class.
    # For detailed information, check PhiExt class.
    
    def test_calculate(self):
        
        initial_magnetic_flux = np.random.randint(MINIMUM_MAGNETIC_FLUX,\
                                                    MAXIMUM_MAGNETIC_FLUX)
        final_magnetic_flux = np.random.randint(MINIMUM_MAGNETIC_FLUX,\
                                                    MAXIMUM_MAGNETIC_FLUX)
            
        magnetic_flux_interval = [initial_magnetic_flux, final_magnetic_flux]
        magnetic_field_resolution = np.random.randint(MINIMUM_MAGNETIC_FILED_RESOLUTION,\
                                                    MAXIMUM_MAGNETIC_FILED_RESOLUTION)
        
        magnetic_flux_array = phiext(magnetic_flux_interval,\
                                     magnetic_field_resolution)
        magnetic_flux_array = magnetic_flux_array.calculate(magnetic_flux_interval,\
                                     magnetic_field_resolution)
        
        self.assertAlmostEqual(initial_magnetic_flux, magnetic_flux_array[FIRST_ELEMENT])
        self.assertAlmostEqual(final_magnetic_flux, magnetic_flux_array[LAST_ELEMENT])
        self.assertAlmostEqual(magnetic_field_resolution, magnetic_flux_array.size)
        

if __name__ == '__main__':
    unittest.main()