# @ali.akgun
# @date: 24.11.2021
# @to do:
# surface plot !!!  
# @bugs:
# @parameters:
# @brief:
# Plots normalized voltage response of Bi-SQUID against external applied
# magnetic field.

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

NORMALIZEDMAGNETICFLUX = 0
IC3 = 1
NORMALIZEDVOLTAGE = 2
NORMALIZEDVOLTAGE2dPlot = 1

class Plot:
    
    # @ali.akgun
    # @date: 24.11.2021
    # @to do:  
    # @bugs:
    # @parameters:
    #   @output = Consists defined external normalized magnetic flux and 
    # normalized voltage response array.
    #   external applied magnetic field.
    # @brief:
    # constructor method
    
    def __init__ (self, output):
        
        self.output = output
    
    # @ali.akgun
    # @date: 24.11.2021
    # @to do:  
    # @bugs:
    # @parameters:
    #   @output = Consists defined external normalized magnetic flux and 
    # @brief:
    # Plots normalized voltage response of Bi-SQUID against external applied
    # magnetic field.
    
    def plot(self, output):
        
        
       plt.plot(output[NORMALIZEDMAGNETICFLUX], output[NORMALIZEDVOLTAGE2dPlot])
       plt.xlabel("PhiExternal")
       plt.ylabel("V(PhiExternal)")
       plt.title("Voltage-magnetic flux")
       plt.grid()
       plt.show()
       

    # @ali.akgun
    # @date: 24.11.2021
    # @to do:  
    # @bugs:
    # @parameters:
    #   @voltage = normalized voltage response of Bi-SQUID against 
    #   external applied magnetic field.
    #   @input_file = Simulation input csv file.
    # @brief:
    # Surface plot method to plot normalized voltage response of Bi-SQUID
    # against external applied magnetic field.
    
    def surface_plot(self, output):
        
        fig, ax = plt.subplots(subplot_kw = {"projection": "3d"})

        X = output[NORMALIZEDMAGNETICFLUX]
        Y = output[IC3]
        X, Y = np.meshgrid(X, Y)
        Z = output[NORMALIZEDVOLTAGE]

        # Plot the surface.
        surf = ax.plot_surface(X, Y, Z, cmap = cm.coolwarm,
                       linewidth=0, antialiased=False)

        # Customize the z axis.
        # ax.set_zlim(-1.01, 1.01)
        # ax.zaxis.set_major_locator(LinearLocator(10))
        # A StrMethodFormatter is used automatically
        ax.zaxis.set_major_formatter('{x:.02f}')
        fig.colorbar(surf, shrink=0.5, aspect=5)

        plt.show()