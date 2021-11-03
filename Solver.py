# @ali.akgun
# @date: 29.08.2021
# @to do:
# @bugs:
# @parameters:
# @brief:
# Solves Bi-SQUID systems of equations.

import numpy as np
from scipy.integrate import odeint


class Solver:
    
    def __init__ (self, initial_conditions, t, PhiExt, ib, l, ic3):
        
        self.initial_conditions = initial_conditions
        self.t = t
        self.PhiExt = PhiExt
        self.ib = ib
        self.l = l
        self.ic3 = ic3
        
    # @ali.akgun
    # @date: 29.08.2021
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
    
    def odes(self, initial_conditions, t, PhiExt, ib, l, ic3):
        
        # constants
        # assign each ODE to a vector element
        theta = initial_conditions[0]
        psi = initial_conditions[1]

        # define each ODE
        dthetadt = ib - (2 * np.sin(theta / 2) * np.cos(psi / 2))
        dpsidt = (-2 * ((PhiExt + psi) / l) - 2 * ic3 * np.sin(psi)\
                  -(2 * np.sin(psi / 2) * np.cos(theta / 2))) / 3

        return [dthetadt, dpsidt]

    # @ali.akgun
    # @date: 29.08.2021
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
    
    def calculate (self, initial_conditions, t, PhiExt, ib, l, ic3):
        
        return odeint(self.odes, initial_conditions, t,\
                      args = (PhiExt, ib, l, ic3))