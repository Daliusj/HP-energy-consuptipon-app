import pandas as pd
import numpy as np


df = pd.read_csv('Temp data 2022.csv')
df['Power'] = 0


def heatpump_power(power, lower_t, temp=-23):
    x = [temp, 20]
    y = [power, 0]
    return np.interp(lower_t, x, y)


def energy_consumption(power, lower_t=20, temp=-23):
    x = [temp, 20]
    y = [power, 0]
    heat_hourly = []
    for index, row in df.iterrows():
        if row['Temperature'] < lower_t:
            x_new = float(row['Temperature'])
            print(x_new)
            y_new = np.interp(x_new, x, y)
            df.loc[index, 'Power'] = y_new
            heat_hourly.append(y_new)
    df.to_csv('data_output.csv')
    return round(sum(heat_hourly), 2)
