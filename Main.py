#############################################################################################
# @author: ali.akgun
# @date: 16.09.2021
# @brief:
#  Main python file of pySQIF
# @to-do:
#  You should create clasesses for output data generation and visualization !!! >>> Surface plot
#  her method input file input olarak alsa, bu input file dan seçse inputları ?!
#  record voltage outputs as a text file externally.
#  Classlardaki methodlarda bulunan her işi ufak ufak methodlara böl !!!
# değişkenleri class içinde gerekirse private tanımla hepsi import edilince
# çakışmalar olabilir !!!
# Time resolution problemi 
# @bugs: There is no known bugs.
##############################################################################################


from Plot import *

from PySQIF import *

v = PySQIF("input.csv")
v = v.calculate("input.csv")

plot = Plot(v)
plot = plot.plot(v)
