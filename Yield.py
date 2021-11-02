from PhiExt import *
from Voltage import *
from Period import *
from YieldIc3 import *

characteristic_voltage = 1 # Characteristic voltage, mV
initial = 0
final = 2 * np.pi
magnetic_field_sample = 200
initial_conditions = [0, 0]
ib = 2 # Ib / Ic
l = 1.4 # 2πIcL / Phi_0
ic3 = 5 # Ic3 / Ic
TimeDataPoints = 100
standard_deviation = 0.1 # standard deviation
number_of_runs = 10 # number of runs

t = Period(characteristic_voltage, TimeDataPoints)
t = t.calculate(characteristic_voltage, TimeDataPoints)
PhiExtArray = PhiExt(initial, final, magnetic_field_sample)
PhiExtArray = PhiExtArray.calculate(initial, final, magnetic_field_sample)

yield_ic3 = YieldIc3(standard_deviation, number_of_runs,\
                  magnetic_field_sample, initial_conditions, t, PhiExtArray,\
                      ib, l, ic3)
    
yield_ic3  = yield_ic3.calculate(standard_deviation, number_of_runs,\
                  magnetic_field_sample, initial_conditions, t, PhiExtArray,\
                      ib, l, ic3)

            