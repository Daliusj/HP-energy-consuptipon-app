import streamlit as st
from backend import energy_consumption as ec
from backend import gas_consumption as gc
# from backend import gas_price as gp
from backend import heatpump_power as hp
from backend import electricity_consumption as elc

# st.set_page_config(layout="wide")

power_temp = st.number_input(label='Lowest temperature used for power calculation, C: ', value=-23)
heatpump_lower_temp = st.number_input(label='Heatpump lowest working temperature, C: ', value=-10)
power_input = st.number_input(label=f'Heating power, kw @ {power_temp}C: ')


st.text(f'Power @ {heatpump_lower_temp}C outside (interpolated): {round(hp(power=power_input, lower_t=heatpump_lower_temp, temp=power_temp), 2)} kW')

st.subheader('Without heatpump')
energy_no_hp = ec(power=power_input, temp=power_temp)
st.text(f'Energy consumption for heating: {energy_no_hp} kWh')
gas_consumption_no_hp = gc(energy_no_hp)
st.text(f'Gas consumption for heating without heatpump: {gas_consumption_no_hp} m3. ')
# st.text(f'Gas price: {gp(gc(energy))} Eur')

st.subheader('With heatpump')
energy_with_hp = ec(power=power_input, lower_t=heatpump_lower_temp, temp=power_temp)
gas_consumption_hp = gc(energy_with_hp)
st.text(f'Gas consumption with heatpump: {gas_consumption_hp} m3.')
# st.text(f'Gas price: {gp(gc(energy))} Eur')
st.text(f'Gas saving {round((gas_consumption_no_hp - gas_consumption_hp), 2)} m3')

energy_hp = energy_no_hp - energy_with_hp
st.text(f'Electricity consumption (COP = 2.4): {elc (energy_hp)} kWh')
