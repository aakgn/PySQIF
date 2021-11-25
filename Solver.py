# @ali.akgun
# @date: 24.11.2021
# @to do:
# for loop içindeki sabit hesaplamaları for loop dşında yap performans arttırmak
# için
# calculate methodunu böl örnek bir method psi1 hesaplasın 
# diğer method psi 2 sonra toplasın falan
# @bugs:
# @parameters:
# @brief:
# Solves Bi-SQUID systems of differential equations.

import numpy as np
from scipy.integrate import odeint


class Solver:
    
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
    # @brief:
    # constructor method
    
    def __init__ (self, psi_initial, t, PhiExt, ib, ic3, beta, l12s, l12d,\
                  l23s, d):
        
        self.psi_initial = psi_initial
        self.t = t
        self.PhiExt = PhiExt
        self.ib = ib
        self.ic3 = ic3
        self.beta = beta
        self.l12s = l12s
        self.l12d = l12d
        self.l23s = l23s
        self.d = d
   
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
    # @brief:
    # Returns systems of differential equations as dpsi1dt and dpsi2dt.
    
    def odes(self, psi_initial, t, PhiExt, ib, ic3, beta, l12s, l12d, l23s, d):
        
        
        # constants

        # assign each ODE to a vector element
        psi1 = psi_initial[0]
        psi2 = psi_initial[1]

        # define each ODE
        dpsi1dt = (1 + ((l12d * d) / (d * l12s))) * (ib / 2) - (1 / (d * l12s * beta))\
            * (psi1 - psi2 - 2 * np.pi * PhiExt * beta) + (1 / d) *\
            (1 + (l23s / (d * l12s))) * ic3 * np.sin(psi2 - psi1) - (1 / 2) * \
            (1 + (1 / d)) * np.sin(psi1) - (1 / 2) * (1 - (1 / d)) * np.sin(psi2)

        dpsi2dt = (1 + ((l12d * d) / (d * l12s))) * (ib / 2) + (1 / (d * l12s * beta))\
            * (psi1 - psi2 - 2 * np.pi * PhiExt * beta) - (1 / d) *\
            (1 + (l23s / (d * l12s))) * ic3 * np.sin(psi2 - psi1) - (1 / 2) * \
            (1 - (1 / d)) * np.sin(psi1) - (1 / 2) * (1 + (1 / d)) * np.sin(psi2)

        return [dpsi1dt, dpsi2dt]

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
    # @brief:
    # Solves systems of differential equations for Bi-SQUID
    
    def calculate (self, psi_initial, t, PhiExt, ib, ic3, beta, l12s, l12d, l23s, d):
        
        return odeint(self.odes, psi_initial, t,\
                      args = (PhiExt, ib, ic3, beta, l12s, l12d, l23s, d))