import matplotlib.pyplot as plt
from Alpha import *
from Period import *
from Voltage import *
from PlasmaFrequency import *


critical_current = 100e-6 #A
initial_alpha = 0
final_alpha = 2.25
alpha_data_points = 100
simulation_time_constant = 100
alpha = Alpha(initial_alpha, final_alpha, alpha_data_points)
alpha = alpha.calculate()

capacitance = 0.2e-12 #F
w_junction = PlasmaFrequency(critical_current, capacitance)
w_junction = w_junction.calculate()
time_data_points = 100
t = Period(w_junction, time_data_points,\
           simulation_time_constant)
t = t.calculate()

initial_conditions = [0, 0]
beta_junction = 0.9

average_voltage = Voltage(initial_conditions, alpha, t, beta_junction)
average_voltage = average_voltage.calculate()
average_voltage = average_voltage * H_BAR / (2 * E)
average_voltage = average_voltage * w_junction 
normalized_voltage = average_voltage / critical_current
resistance = 200
normalized_voltage = normalized_voltage / resistance

plt.plot(normalized_voltage, alpha)
plt.xlabel("V")
plt.ylabel("I / Ic")
plt.grid()
