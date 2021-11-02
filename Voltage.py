# @ali.akgun
# @date: 02.11.2021
# @to do:
# Boşuna hem plot hem calculation oluşturuyorsun onu düzenle boşuna complexity !!!    
# @bugs:
# @parameters:
# @brief:
# Calculates normalized voltage.

import numpy as np
from scipy.integrate import odeint
from Solver import *
import matplotlib.pyplot as plt
from statistics import mean

class Voltage:
    
    def __init__ (self, initial_conditions, t, PhiExtArray, ib, l, ic3,\
                  data_points):
        
        self.initial_conditions = initial_conditions
        self.t = t
        self.PhiExtArray = PhiExtArray
        self.ib = ib
        self.l = l
        self.ic3 = ic3
        self.data_points = data_points
        
    # @ali.akgun
    # @date: 29.08.2021
    # @to do:
    # @bugs:
    # @parameters:
    #   initial_conditions = initial conditions for solving systems of d.e.
    #   t = time interval of system.
    #   PhiExtArray = External magnetic field array as phiext/phi0
    #   ib = bias current
    #   l = Inductance parameter(not exactly equal to inductance !!!)
    #   ic3 = Ic3 / Ic, Normalized current through shunt junction.
    #   data_points = Total data points of normalized voltage array
    # @brief:
    # Returns normalized voltage mean(voltage) = (1/2) * mean(thetadot)
    
    def calculate(self, initial_conditions, t, PhiExtArray, ib, l, ic3,\
                  data_points):
 
        system = Solver(initial_conditions, t, PhiExtArray, ib, l, ic3)
        meanthetadot = []
        meanpsidot = []
        for i in range(data_points):
    
            PhiExt = PhiExtArray[i]
            x = system.calculate(initial_conditions, t, PhiExt, ib, l, ic3)
            theta = x[:,0]
            psi = x[:,1]
            thetadot = ib - (2 * np.sin(theta / 2) * np.cos(psi / 2))
            psidot = (-2 * ((PhiExt + psi) / l) - 2 * ic3 * np.sin(psi) -\
                      (2 * np.sin(psi / 2) * np.cos(theta / 2))) / 3
    
            meanthetadot.append(mean(thetadot))
            meanpsidot.append(mean(psidot))
        return np.array(meanthetadot) / 2
    
    # @ali.akgun
    # @date: 29.08.2021
    # @to do:
    # @bugs:
    # @parameters:
    #   initial_conditions = initial conditions for solving systems of d.e.
    #   t = time interval of system.
    #   PhiExtArray = External magnetic field array as phiext/phi0
    #   ib = bias current
    #   l = Inductance parameter(not exactly equal to inductance !!!)
    #   ic3 = Ic3 / Ic, Normalized current through shunt junction.
    #   data_points = Total data points of normalized voltage array
    # @brief:
    # Plots meanthetadot(normalized voltage) vs 
    # normalized external magnetic field.
    
    def plot(self, initial_conditions, t, PhiExtArray, ib, l, ic3,\
             data_points):
       # neden teorik olarak y eksenine göre simetri olduğunu varsaydığımda 
       # deneysel sonuçları sağlıyor !?!
       plt.plot(PhiExtArray, self.calculate(initial_conditions, t,\
                    PhiExtArray, ib, l, ic3, data_points))
       plt.xlabel("PhiExternal")
       plt.ylabel("V(PhiExternal)")
       plt.title("Voltage-magnetic flux")
       plt.grid()
       plt.show()