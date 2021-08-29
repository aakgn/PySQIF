from PhiExt import *
from Voltage import *
from Period import *
characteristic_voltage = 1 # Characteristic voltage, mV
initial = 0
final = 2 * np.pi
data_points = 200
initial_conditions = [0, 0]
ib = 2
l = 1.4
ic3 = 1
TimeDataPoints = 100

t = Period(characteristic_voltage, TimeDataPoints)
t = t.calculate(characteristic_voltage, TimeDataPoints)
PhiExtArray = PhiExt(initial, final, data_points)
PhiExtArray = PhiExtArray.calculate(initial, final, data_points)
voltage = Voltage(initial_conditions, t, PhiExtArray, ib, l, ic3, data_points)
voltage.plot(initial_conditions, t, PhiExtArray, ib, l, ic3, data_points)
    
    
