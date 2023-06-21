import pandas as pd
import numpy as np

# KWh/m3
NATURAL_GAS_CALORIFIC_VALUE = 9.6

# Eur
GAS_PRICE = 1.197

# COP@-10C
COP = 2.4


def heatpump_power(power, lower_t=20, temp=-23):
    x = [temp, 20]
    y = [power, 0]
    return np.interp(lower_t, x, y)


def energy_consumption(power, lower_t=20, temp=-23):
    df = pd.read_csv('Temp_Output_hourly.csv')
    x = [temp, 20]
    y = [power, 0]
    heat_hourly = []
    for index, row in df.iterrows():
        if row['Temperature'] < lower_t:
            x_new = float(row['Temperature'])
            y_new = np.interp(x_new, x, y)
            heat_hourly.append(y_new)
    df2 = pd.DataFrame(heat_hourly)
    df2.to_csv('power_output.csv', index=False)
    return round(sum(heat_hourly), 2)


def gas_consumption(energy):
    return round((energy / NATURAL_GAS_CALORIFIC_VALUE), 2)


def gas_price(gas):
    return round((gas * GAS_PRICE), 2)


def electricity_consumption(energy):
    return round((energy / COP), 2)




