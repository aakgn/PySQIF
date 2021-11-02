from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from statistics import *

ib = 2
l = 1.4
ic3 = 1
vc = 1 # Characteristic voltage, mV
phi0inv = 483e9 # 483GHz/mV, inverse phi0
wc = (2 * np.pi) * phi0inv * vc # 
T = 2 * np.pi / wc


def odes(x, t, PhiExt, ib, l, ic3):
    # constants

    # assign each ODE to a vector element
    theta = x[0]
    psi = x[1]

    # define each ODE
    dthetadt = ib - (2 * np.sin(theta / 2) * np.cos(psi / 2))
    dpsidt = (-2 * ((PhiExt + psi) / l) - 2 * ic3 * np.sin(psi)\
        -(2 * np.sin(psi / 2) * np.cos(theta / 2))) / 3

    return [dthetadt, dpsidt]


x0 = [0, 0]
# multiplier 27 determinates period of the problem. 
t = np.linspace(0,  T * 40, 100) * wc
meanthetadot = []
meanpsidot = []
PhiExtArray = np.linspace(0, 4 * np.pi, 200)
for i in range(200):
    
    PhiExt = PhiExtArray[i]
    x = odeint(odes, x0, t, args = (PhiExt, ib, l, ic3))
    theta = x[:,0]
    psi = x[:,1]
    thetadot = ib - (2 * np.sin(theta / 2) * np.cos(psi / 2))
    psidot = (-2 * ((PhiExt + psi) / l) - 2 * ic3 * np.sin(psi) -\
        (2 * np.sin(psi / 2) * np.cos(theta / 2))) / 3
    
    meanthetadot.append(mean(thetadot))
    meanpsidot.append(mean(psidot))
    
    
# neden teorik olarak y eksenine göre simetri olduğunu varsaydığımda deneysel
# sonuçları sağlıyor !?!
plt.plot(PhiExtArray, np.array(meanthetadot) / 2, "r.",\
          -PhiExtArray + 4 * np.pi, np.array(meanthetadot) / 2, "r.")
#plt.plot(PhiExtArray, np.array(meanthetadot) / 2, "r.")
plt.xlabel("PhiExternal")
plt.ylabel("V(PhiExternal)")
plt.title("Voltage-magnetic flux")
plt.grid()
plt.show()