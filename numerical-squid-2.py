from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from statistics import *

ib = 2
ic3 = 0.4
vc = 1 # Characteristic voltage, mV
phi0inv = 483e9 # 483GHz/mV, inverse phi0
wc = (2 * np.pi) * phi0inv * vc # 
T = 2 * np.pi / wc

beta = 1
l1a = 0.27
l1b = 0.27
l2a = 0.24
l2b = 0.24
l3a = 0.3
l3b = 0.3

l12s = l1a + l1b + l2a + l2b
l12d = l1b - l1a + l2b - l2a
l23s = l2a + l2b + l3a + l3b
d = 3 + ((2 * l23s) / l12s) 


def odes(psi_initial, t, PhiExt, ib, ic3, beta, l12s, l12d, l23s, d):
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


psi_initial = [0, 0]
# multiplier 27 determinates period of the problem. 
t = np.linspace(0,  T * 40, 200) * wc
meanvoltage = []
PhiExtArray = np.linspace(0, 1, 200)
for i in range(200):
    
    PhiExt = PhiExtArray[i]
    x = odeint(odes, psi_initial, t, args = (PhiExt, ib, ic3, beta, l12s, l12d, l23s, d))
    psi1 = x[:,0]
    psi2 = x[:,1]
    
    dpsi1dt = (1 + ((l12d * d) / (d * l12s))) * (ib / 2) - (1 / (d * l12s * beta))\
        * (psi1 - psi2 - 2 * np.pi * PhiExt * beta) + (1 / d) *\
        (1 + (l23s / (d * l12s))) * ic3 * np.sin(psi2 - psi1) - (1 / 2) * \
        (1 + (1 / d)) * np.sin(psi1) - (1 / 2) * (1 - (1 / d)) * np.sin(psi2)

    dpsi2dt = (1 + ((l12d * d) / (d * l12s))) * (ib / 2) + (1 / (d * l12s * beta))\
        * (psi1 - psi2 - 2 * np.pi * PhiExt * beta) - (1 / d) *\
        (1 + (l23s / (d * l12s))) * ic3 * np.sin(psi2 - psi1) - (1 / 2) * \
        (1 - (1 / d)) * np.sin(psi1) - (1 / 2) * (1 + (1 / d)) * np.sin(psi2)
    
    meanvoltage.append(mean(dpsi1dt + dpsi2dt) / 2)
    
    
# neden teorik olarak y eksenine göre simetri olduğunu varsaydığımda deneysel
# sonuçları sağlıyor !?!
plt.plot(PhiExtArray, np.array(meanvoltage))
#plt.plot(PhiExtArray, np.array(meanthetadot) / 2, "r.")
plt.xlabel("PhiExternal")
plt.ylabel("V(PhiExternal)")
plt.title("Voltage-magnetic flux")
plt.grid()
plt.show()