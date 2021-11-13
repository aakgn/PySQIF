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
    
    def __init__ (self, psi_initial, t, phi_ext_array, ib, ic3, beta, l12s, l12d,\
                  l23s, d, data_points):
        
        self.psi_initial = psi_initial
        self.t = t
        self.phi_ext_array = phi_ext_array
        self.ib = ib
        self.ic3 = ic3
        self.beta = beta
        self.l12s = l12s
        self.l12d = l12d
        self.l23s = l23s
        self.d = d
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
    
    def calculate(self, psi_initial, t, phi_ext_array, ib, ic3, beta, l12s, l12d,\
                  l23s, d, data_points):
 
        system = Solver(psi_initial, t, phi_ext_array, ib, ic3, beta, l12s, l12d,\
                      l23s, d)
        meanvoltage = []
        for i in range(data_points):
    
            phi_ext = phi_ext_array[i]
            x = system.calculate(psi_initial, t, phi_ext, ib, ic3, beta, l12s,\
                                 l12d, l23s, d)
            psi1 = x[:,0]
            psi2 = x[:,1]
            
            dpsi1dt = (1 + ((l12d * d) / (d * l12s))) * (ib / 2) - (1 / (d * l12s * beta))\
                * (psi1 - psi2 - 2 * np.pi * phi_ext * beta) + (1 / d) *\
                (1 + (l23s / (d * l12s))) * ic3 * np.sin(psi2 - psi1) - (1 / 2) * \
                (1 + (1 / d)) * np.sin(psi1) - (1 / 2) * (1 - (1 / d)) * np.sin(psi2)

            dpsi2dt = (1 + ((l12d * d) / (d * l12s))) * (ib / 2) + (1 / (d * l12s * beta))\
                * (psi1 - psi2 - 2 * np.pi * phi_ext * beta) - (1 / d) *\
                (1 + (l23s / (d * l12s))) * ic3 * np.sin(psi2 - psi1) - (1 / 2) * \
                (1 - (1 / d)) * np.sin(psi1) - (1 / 2) * (1 + (1 / d)) * np.sin(psi2)
    
            meanvoltage.append(mean(dpsi1dt + dpsi2dt) / 2)
        
        return meanvoltage 
    
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
    
    def plot(self, psi_initial, t, phi_ext_array, ib, ic3, beta, l12s, l12d,\
                  l23s, d, data_points):
       # neden teorik olarak y eksenine göre simetri olduğunu varsaydığımda 
       # deneysel sonuçları sağlıyor !?!
       plt.plot(phi_ext_array, self.calculate(psi_initial, t, phi_ext_array, ib, ic3, beta,\
                              l12s, l12d, l23s, d, data_points))
       plt.xlabel("PhiExternal")
       plt.ylabel("V(PhiExternal)")
       plt.title("Voltage-magnetic flux")
       plt.grid()
       plt.show()