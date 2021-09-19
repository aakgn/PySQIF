from PhiExt import *
from Voltage import *
from Period import *

characteristic_voltage = 1 # Characteristic voltage, mV
initial = 0
final = 2 * np.pi
data_points = 200
initial_conditions = [0, 0]
ib = 2 # Ib / Ic
l = 1.4 # 2πIcL / Phi_0
ic3 = 1 # Ic3 / Ic
TimeDataPoints = 100

t = Period(characteristic_voltage, TimeDataPoints)
t = t.calculate(characteristic_voltage, TimeDataPoints)
PhiExtArray = PhiExt(initial, final, data_points)
PhiExtArray = PhiExtArray.calculate(initial, final, data_points)

    

SD = 0.2 # standard deviation
RUNNUM = 1 # number of runs

parameter_distribution = np.random.normal(ic3, SD, RUNNUM)
# plt.figure(1)
# plt.hist(ib_distribution, 101, density=True, facecolor='g', alpha=0.75)
# plt.hist(parameter_distribution, 100, facecolor='g', alpha=0.75)
# plt.xlabel("ib")
# plt.ylabel("frequency")
# plt.title("ib distribution")
# plt.grid()
# plt.show()


voltage_margin = np.empty((RUNNUM, data_points))
for i in range(RUNNUM):
    
    parameter = parameter_distribution[i]
    voltage = Voltage(initial_conditions, t, PhiExtArray, ib, l, parameter,\
                      data_points)
    voltage_margin[i, :] = voltage.calculate(initial_conditions,\
                    t, PhiExtArray, ib, l, parameter, data_points)
            