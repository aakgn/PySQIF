#############################################################################################
# @author: ali.akgun
# @date: 16.09.2021
# @brief:
#  Main python file of PySQUID
# @to-do:
#  Should make improvements on Bi-SQUID voltage response visualization. Visualization of
#  voltage response is not smooth due to differential equations solver algorithm.(i think)
#  You should run this simulator and see what is best !!! :)
#  You should fix Bi-SQUID period problem !!!
#  You should create clasesses for output data generation and visualization !!!
#  You should start to generate graphical user interface !!!
#  her method input file input olarak alsa, bu input file dan seçse inputları ?!
#  record voltage outputs as a text file externally.
# @bugs: There is no known bugs.
##############################################################################################

from PySQUID import *
from Plot import *

v = PySQUID("input.csv")
v = v.calculate("input.csv")

plot = Plot(v, "input.csv")
plot = plot.plot(v, "input.csv")
