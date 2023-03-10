import streamlit as st
from backend import energy_consumption as ec
from backend import gas_consumption as gc
from backend import gas_price as gp

#st.set_page_config(layout="wide")

power_input = st.number_input(label='Heating power, kw @ -23C: ')
power_temp = st.number_input(label='Lowest temperature used for power calculation, C: ', value=-23)
heatpump_lower_temp = st.number_input(label='Heatpump lowest working temperature, C: ', value=-10)

st.subheader('Without heatpump')
st.text(f'Energy consumption for heating: {ec(power=power_input, temp=power_temp)} kWh')
st.text(f'Gas consumption for heating without heatpump: {gc(ec(power=power_input, temp=power_temp))} m3. ')
st.text(f'Gas price: {gp(gc(ec(power=power_input, temp=power_temp)))} Eur')

st.subheader('Wit heatpump')
st.text(f'Gas consumption with heatpump: {gc(ec(power=power_input, lower_t=heatpump_lower_temp, temp=power_temp))} m3.')
st.text(f'Gas price: {gp(gc(ec(power=power_input, lower_t=heatpump_lower_temp, temp=power_temp)))} Eur')
st.text(f'Gas saving {round((gc(ec(power=power_input, temp=power_temp)) - gc(ec(power=power_input, lower_t=heatpump_lower_temp, temp=power_temp))), 2)} m3')
