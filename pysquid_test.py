import unittest
from PySQUID import *


characteristic_voltage = 1 # Characteristic voltage, mV
magnetic_field_range = [0, 1]
magnetic_field_resolution = 60
psi_initial = [0, 0]
ib = 2 # Ib / Ic
ic3 = 0 # Ic3 / Ic
time_resolution = 300
beta = 1
l1a = 0.27
l1b = 0.27
l2a = 0
l2b = 0
l3a = 0
l3b = 0

l12s = l1a + l1b + l2a + l2b
l12d = l1b - l1a + l2b - l2a
l23s = l2a + l2b + l3a + l3b
d = 3 + ((2 * l23s) / l12s) 


class MultiplicationTestCase(unittest.TestCase):

    def setUp(self):
        self.pysquid = PySQUID(characteristic_voltage, magnetic_field_range,\
                      magnetic_field_resolution, psi_initial, ib, ic3,\
                     beta, l12s, l12d, l23s, d, time_resolution)

    def test_run(self):
        result = self.pysquid.calculate(characteristic_voltage, magnetic_field_range,\
                      magnetic_field_resolution, psi_initial, ib, ic3,\
                     beta, l12s, l12d, l23s, d, time_resolution)

    
    def test_negative_voltage(self):
        
        result = self.pysquid.calculate(characteristic_voltage,\
            magnetic_field_range, magnetic_field_resolution,\
            psi_initial, ib, ic3, beta, l12s, l12d, l23s, d, time_resolution)
            
        for voltage in range(len(result)):
            self.assertGreater(result[voltage], -0.1, "negative voltage !!!")


if __name__ == '__main__':
    unittest.main()