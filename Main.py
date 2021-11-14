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
#  you should change data points as magnetic field sampling !!!
# initial conditions kısmını user a sormasan olur ne anlasın user :D/ aynı şekilde time ve
# magnetic field resolution !!!Bunlar optional inputlar olabilir default değerler girersin
# kullanıcıdan optional alrısın !!!
# netlsit şekiklde kullanıcıdan input alsın !!!
# netlistte default olsun diferansiyel denklemelrle ilgili olan teknik verielr.
# @bugs: There is no known bugs.
##############################################################################################

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

v = PySQUID(characteristic_voltage, magnetic_field_range,\
              magnetic_field_resolution, psi_initial, ib, ic3,\
             beta, l1a, l1b, l2a, l2b, l3a, l3b, time_resolution)
v = v.calculate(characteristic_voltage, magnetic_field_range,\
              magnetic_field_resolution, psi_initial, ib, ic3,\
             beta, l1a, l1b, l2a, l2b, l3a, l3b, time_resolution)
