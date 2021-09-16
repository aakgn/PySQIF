#############################################################################################
# @author: ali.akgun
# @date: 16.09.2021
# @brief:
#  Main python file of PySQUID
# @to-do:
#  Should make improvements on Bi-SQUID voltage response visualization. Visualization of
#  voltage response is not smooth due to differential equations solver algorithm.(i think)
#  You should run this simulator and see what is best !!! :)
#  You should fix Bi-SQUID period problem !!!
#  You should create clasesses for output data generation and visualization !!!
#  You should start to generate graphical user interface !!!
#  You should integrate SQUID classes into the PySQUID project. (problem is Bi-SQUID time
#  based and SQUID is static, you can do SQUID as time based and you can use same classes
#  for both SQUID and Bi-SQUID.)
# @bugs: There is no known bugs.
##############################################################################################

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
