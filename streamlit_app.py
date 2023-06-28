import streamlit as st
from backend import energy_consumption as ec
from backend import heatpump_power as hp

power_temp = st.number_input(label='Lowest temperature used for power calculation, C: ', value=-23)
heatpump_lower_temp = st.number_input(label='Heatpump lowest working temperature, C: ', value=-10)
power_input = st.number_input(label=f'Heating power, kw @ {power_temp}C: ')


st.text(f'Power @ {heatpump_lower_temp}C outside (interpolated): {round(hp(power=power_input, lower_t=heatpump_lower_temp, temp=power_temp), 2)} kW')

st.subheader('Without heatpump')
energy_no_hp = ec(power=power_input, temp=power_temp)
st.text(f'Energy consumption for heating: {round((energy_no_hp / 1000), 2)} MWh')

st.subheader('With heatpump')
energy_with_hp = ec(power=power_input, lower_t=heatpump_lower_temp, temp=power_temp)

st.text(f'Energy consumption for heating with heatpump: {round((energy_with_hp / 1000), 2)} MWh.')

