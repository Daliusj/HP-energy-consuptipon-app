import pandas as pd
import numpy as np

NATURAL_GAS_CALORIFIC_VALUE = 9.6
GAS_PRICE = 1.197


def energy_consumption(power, lower_t=20, temp=-23):
    df = pd.read_csv('Temp_Output_hourly.csv')
    x = [temp, 20]
    y = [power, 0]
    powers_hourly = []
    for index, row in df.iterrows():
        if float(row['Temperature'] < lower_t):
            x_new = float(row['Temperature'])
            y_new = np.interp(x_new, x, y)
            powers_hourly.append(y_new)
    df2 = pd.DataFrame(powers_hourly)
    df2.to_csv('power_output.csv', index=False)
    return round(sum(powers_hourly), 2)


def gas_consumption(energy):
    return round((energy / NATURAL_GAS_CALORIFIC_VALUE), 2)


def gas_price(gas):
    return round((gas * GAS_PRICE), 2)
