# @ali.akgun
# @date: 13.11.2021
# @to do:
# @bugs:
# @parameters:
# @brief:
# Solves Bi-SQUID systems of differential equations.

import numpy as np
from scipy.integrate import odeint


class Solver:
    
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
    # @date: 13.11.2021
    # @to do:
    # @bugs:
    # @parameters:
    #   initial_conditions = initial conditions for solving systems of d.e.
    #   t = time steps of system.(sampling)
    #   PhiExt = External magnetic field as phiext/phi0
    #   ib = Normalized bias current Ib / Ic
    #   l = Inductance parameter (2πIcL / Phi_0)
    #   ic3 = Ic3 / Ic, Normalized current through shunt junction.
    # @brief:
    # Returns systems of differential equations as
    # dpsidt and dthetadt.
    
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
    # @date: 13.11.2021
    # @to do:
    # @bugs:
    # @parameters:
    #   initial_conditions = initial conditions for solving systems of d.e.
    #   t = time interval of system.
    #   PhiExt = External magnetic field as phiext/phi0
    #   ib = bias current
    #   l = Inductance parameter(not exactly equal to inductance !!!)
    #   ic3 = Ic3 / Ic, Normalized current through shunt junction.
    # @brief:
    # Solves systems of differential equations for Bi-SQUID
    
    def calculate (self, psi_initial, t, PhiExt, ib, ic3, beta, l12s, l12d, l23s, d):
        
        return odeint(self.odes, psi_initial, t,\
                      args = (PhiExt, ib, ic3, beta, l12s, l12d, l23s, d))