# @ali.akgun
# @date: 24.11.2021
# @to do:  
# for loop içindeki sabit hesaplamaları for loop dşında yap performans arttırmak
# calculate methodunu böl örnek bir method psi1 hesaplasın 
# diğer method psi 2 sonra toplasın falan
# için
# @bugs:
# @parameters:
# @brief:
# Calculates normalized voltage response of Bi-SQUID against external applied
# magnetic field.

import numpy as np
from scipy.integrate import simps
from statistics import mean

try:
    # When running from pip installation
    from .Solver import *
except ImportError:
    # When running from source without pip installation
    from Solver import *

class Voltage:
    
    
    # @ali.akgun
    # @date: 24.11.2021
    # @to do:  
    # @bugs:
    # @parameters:
    #   @psi_cinitial = initial conditions for solving systems of d.e. 
    #   (psi1 and psi2)
    #   @t = time step array for solving systems of differential equations.
    #   @phi_ext_array = Normalized External applied magnetic field array as 
    #   phiext/phi0
    #   @ib = Normalized bias current (Ib / Ic)
    #   ic3 = Ic3 / Ic, Normalized current through shunt junction.
    #   @l12s = l1a + l1b + l2a + l2b
    #   @l12d = l1b – l1a + l2b – l2a
    #   @l23s = l2a + l2b + l3a + l3b
    #   @d =    3 + 2l23s / l12s
    #   @magnetic_field_resolution = Represents length of external applied
    #   magnetic field array
    # @brief:
    # constructor method
    
    def __init__ (self, psi_initial, t, phi_ext_array, ib, ic3, beta, l12s, l12d,\
                  l23s, d, magnetic_field_resolution):
        
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
        self.magnetic_field_resolution = magnetic_field_resolution
     
    # @ali.akgun
    # @date: 24.11.2021
    # @to do:  
    # Write brief !!!
    # @bugs:
    # @parameters:
    #   @psi_cinitial = initial conditions for solving systems of d.e. 
    #   (psi1 and psi2)
    #   @t = time step array for solving systems of differential equations.
    #   @phi_ext_array = Normalized External applied magnetic field array as 
    #   phiext/phi0
    #   @ib = Normalized bias current (Ib / Ic)
    #   ic3 = Ic3 / Ic, Normalized current through shunt junction.
    #   @l12s = l1a + l1b + l2a + l2b
    #   @l12d = l1b – l1a + l2b – l2a
    #   @l23s = l2a + l2b + l3a + l3b
    #   @d =    3 + 2l23s / l12s
    #   @magnetic_field_resolution = Represents length of external applied
    #   magnetic field array
    # @brief:

    
    def calculate(self, psi_initial, t, phi_ext_array, ib, ic3, beta, l12s, l12d,\
                  l23s, d, magnetic_field_resolution):
 
        system = Solver(psi_initial, t, phi_ext_array, ib, ic3, beta, l12s, l12d,\
                      l23s, d)
        meanvoltage = []
        for i in range(magnetic_field_resolution):
    
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
            
            meanvoltage.append(simps(dpsi1dt + dpsi2dt, t) /\
              (2 *  t[len(t) - 1]))
        
        return meanvoltage 
