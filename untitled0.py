# @ali.akgun
# @date: 13.11.2021
# @to do:
# Boşuna hem plot hem calculation oluşturuyorsun onu düzenle boşuna complexity !!!    
# @bugs:
# More comments !!!    
# @parameters:
# @brief: Main class

import pandas as pd
input_data = pd.read_csv("input.csv")


psi_initial = [input_data.values[0, 1], input_data.values[1, 1]]
magnetic_field_range = [input_data.values[2, 1], input_data.values[3, 1]]
magnetic_field_resolution = input_data.values[4, 1]
characteristic_voltage = input_data.values[5, 1] 
ib = input_data.values[6, 1]
ic3 = input_data.values[7, 1]
time_resolution = input_data.values[8, 1]
beta = input_data.values[9, 1]
l1a = input_data.values[10, 1]
l1b = input_data.values[11, 1]
l2a = input_data.values[12, 1]
l2b = input_data.values[13, 1]
l3a = input_data.values[14, 1]
l3b = input_data.values[15, 1]



