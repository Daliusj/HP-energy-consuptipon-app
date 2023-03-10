import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = []
y = []

df_temp = pd.read_csv('Temp_Output_hourly.csv')
for index, row in df_temp.iterrows():
    x.append(float(row['Temperature']))

df_power = pd.read_csv('power_output.csv')
for index, row in df_power.iterrows():
    y.append(float(row['0']))

plt.plot(x, y);

plt.xlabel('Lauko oro temp, C')
plt.ylabel('Galia, kW')

plt.title('Galios')

plt.show()