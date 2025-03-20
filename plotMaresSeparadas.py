import pandas as pd
import matplotlib.pyplot as plt

# Function to load and process data
def load_data(file):
    df = pd.read_csv(file, sep=';')
    df['Timestamp'] = pd.to_datetime(df[['YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE', 'SECOND']])
    df = df.sort_values('Timestamp')
    return df

# Load data
df_level = load_data('dados1.csv')
df_astro = load_data('astro_formatado.csv')
df_meteo = load_data('meteo_formatado.csv')

# Create subplot figure
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(12, 8), sharex=True)

# Plot 1: Lagoon Water Level
axes[0].plot(df_level['Timestamp'], df_level['avg_water_l1_ibge'], marker='o', markersize=0, color='b', label='Mean Water Level (IBGE)')
axes[0].set_title('Water Level Variation (IBGE Tide Gauge)', fontsize=14)
axes[0].set_ylabel('Level (cm)', fontsize=12)
axes[0].grid(True, linestyle='--', alpha=0.6)
axes[0].legend()

# Plot 2: Astronomical Tide
axes[2].plot(df_astro['Timestamp'], df_astro['avg_water_l1_ibge'], marker='o', markersize=0, color='g', label='Astronomical Tide')
axes[2].set_title('Astronomical Tide Variation', fontsize=14)
axes[2].set_ylabel('Level (m)', fontsize=12)
axes[2].grid(True, linestyle='--', alpha=0.6)
axes[2].legend()

# Plot 3: Meteorological Tide
axes[1].plot(df_meteo['Timestamp'], df_meteo['avg_water_l1_ibge'], marker='o', markersize=0, color='r', label='Meteorological Tide')
axes[1].set_title('Meteorological Tide Variation', fontsize=14)
axes[1].set_xlabel('Time', fontsize=12)
axes[1].set_ylabel('Level (m)', fontsize=12)
axes[1].grid(True, linestyle='--', alpha=0.6)
axes[1].legend()

# Adjust layout
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
