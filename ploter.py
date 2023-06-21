import psychrochart

# Define chart limits
chart_limits = {
    'db': [10, 35],           # Dry-bulb temperature limits, deg C
    'wb': [8, 28],            # Wet-bulb temperature limits, deg C
    'p': [0.1, 2],            # Pressure limits, atm
    'r': [0, 100],            # Relative humidity limits, %
    'tdp': [5, 30],           # Dew point temperature limits, deg C
    'h': [10, 140],           # Enthalpy limits, kJ/kg
    'w': [0, 0.03],           # Humidity ratio limits, kg H2O/kg dry air
    'v': [0.8, 1.05],         # Specific volume limits, m3/kg dry air
    'tdb_delta': 5,           # Dry-bulb temperature step, deg C
    'p_delta': 0.01,          # Pressure step, atm
    'tdb_count': 26,          # Number of dry-bulb temperature steps
    'p_count': 101,           # Number of pressure steps
}

# Create psychrometric chart
chart = psychrochart.PsychroChart(chart_limits)

# Add data points to chart
chart.plot(ax=)

# Show chart
chart.show()