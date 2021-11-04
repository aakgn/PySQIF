from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from statistics import *

ib = 2
ic3 = 1
vc = 1 # Characteristic voltage, mV
phi0inv = 483e9 # 483GHz/mV, inverse phi0
wc = (2 * np.pi) * phi0inv * vc # 
T = 2 * np.pi / wc
l1a = 0.27
l1b = 0.27
l2a = 0.24
l2b = 0.24
l3a = 0.3
l3b = 0.3
an = 1
l1 = l1a + l1b

def odes(x, t, PhiExt, ib, l1, l1a, l1b, l2a, l2b, l3a, l3b, an, ic3):
    
    # constants
    # assign each ODE to a vector element
    psi1 = x[0]
    psi2 = x[1]
    psi3 = x[2]
    
    eq1 = (l1b * ib) + psi2 - psi1 + (2 * np.pi * PhiExt * an) +\
        (l1 * ic3 * np.sin(psi3)) + (l2b * np.sin(psi2)) - \
        ((l1 + l2a) * np.sin(psi1)) 
        
    eq2 = -(l1a * ib) + psi2 - psi1 + (2 * np.pi * PhiExt * an) +\
        (l1 * ic3 * np.sin(psi3)) - (l2a * np.sin(psi1)) + \
        ((l1 + l2b) * np.sin(psi2))
    
    eq3 = psi2 - psi3 + psi1 - ((l3a + l3b) * ic3 * np.sin(psi3)) - \
        (l2a * np.sin(psi1)) + (l2b * np.sin(psi2))
        

    # define each ODE
    
    dpsi1dt = -(eq1*l1*l3a - eq3*l1**2 - eq1*l1*l2b + eq1*l1*l3b + eq2*l1*l2b + eq1*l3a*l2b - eq2*l3a*l2b + eq1*l2b*l3b - eq2*l2b*l3b)/(l1*(l1*l3a - l1*l2a - l1*l2b + l1*l3b + l2a*l3a + l2a*l3b + l3a*l2b + l2b*l3b))
                                          
    dpsi2dt = (eq1*l1*l2a - eq3*l1**2 - eq2*l1*l2a + eq2*l1*l3a + eq2*l1*l3b - eq1*l2a*l3a + eq2*l2a*l3a - eq1*l2a*l3b + eq2*l2a*l3b)/(l1*(l1*l3a - l1*l2a - l1*l2b + l1*l3b + l2a*l3a + l2a*l3b + l3a*l2b + l2b*l3b))
                                             
    dpsi3dt = (eq3*l1 - eq1*l2a + eq3*l2a - eq2*l2b + eq3*l2b)/(l1*l3a - l1*l2a - l1*l2b + l1*l3b + l2a*l3a + l2a*l3b + l3a*l2b + l2b*l3b)

    return [dpsi1dt, dpsi2dt, dpsi3dt]


x0 = [0, 0, 0]
# multiplier 27 determinates period of the problem. 
t = np.linspace(0,  T * 100, 40) * wc
meanvoltage = []
PhiExtArray = np.linspace(0, 2 * np.pi, 40)
for i in range(40):
    
    PhiExt = PhiExtArray[i]
    x = odeint(odes, x0, t, \
    args = (PhiExt, ib, l1, l1a, l1b, l2a, l2b, l3a, l3b, an, ic3))
        
    psi1 = x[:, 0]
    psi2 = x[:, 1]
    psi3 = x[:, 2]
    
    eq1 = (l1b * ib) + psi2 - psi1 + (2 * np.pi * PhiExt * an) +\
        (l1 * ic3 * np.sin(psi3)) + (l2b * np.sin(psi2)) - \
        ((l1 + l2a) * np.sin(psi1)) 
        
    eq2 = -(l1a * ib) + psi2 - psi1 + (2 * np.pi * PhiExt * an) +\
        (l1 * ic3 * np.sin(psi3)) - (l2a * np.sin(psi1)) + \
        ((l1 + l2b) * np.sin(psi2))
    
    eq3 = psi2 - psi3 + psi1 - ((l3a + l3b) * ic3 * np.sin(psi3)) - \
        (l2a * np.sin(psi1)) + (l2b * np.sin(psi2))
    
    
    dpsi1dt = -(eq1*l1*l3a - eq3*l1**2 - eq1*l1*l2b + eq1*l1*l3b + eq2*l1*l2b + eq1*l3a*l2b - eq2*l3a*l2b + eq1*l2b*l3b - eq2*l2b*l3b)/(l1*(l1*l3a - l1*l2a - l1*l2b + l1*l3b + l2a*l3a + l2a*l3b + l3a*l2b + l2b*l3b))
                                          
    dpsi2dt = (eq1*l1*l2a - eq3*l1**2 - eq2*l1*l2a + eq2*l1*l3a + eq2*l1*l3b - eq1*l2a*l3a + eq2*l2a*l3a - eq1*l2a*l3b + eq2*l2a*l3b)/(l1*(l1*l3a - l1*l2a - l1*l2b + l1*l3b + l2a*l3a + l2a*l3b + l3a*l2b + l2b*l3b))
                                             
    dpsi3dt = (eq3*l1 - eq1*l2a + eq3*l2a - eq2*l2b + eq3*l2b)/(l1*l3a - l1*l2a - l1*l2b + l1*l3b + l2a*l3a + l2a*l3b + l3a*l2b + l2b*l3b)
    
    meanvoltage.append(mean(dpsi1dt + dpsi2dt))
    
    
# neden teorik olarak y eksenine göre simetri olduğunu varsaydığımda deneysel
# sonuçları sağlıyor !?!
plt.plot(PhiExtArray, np.array(meanvoltage) / 2, "r.")
#plt.plot(PhiExtArray, np.array(meanthetadot) / 2, "r.")
plt.xlabel("PhiExternal")
plt.ylabel("V(PhiExternal)")
plt.title("Voltage-magnetic flux")
plt.grid()
plt.show()