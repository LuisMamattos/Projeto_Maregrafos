import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading the files
df_lagoa = pd.read_csv('dados_resampled.csv', sep=';')
df_meteo = pd.read_csv('meteo_formatado.csv', sep=';')

# Converting date and time columns to datetime
df_lagoa['DATE'] = pd.to_datetime(df_lagoa[['YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE', 'SECOND']])
df_meteo['DATE'] = pd.to_datetime(df_meteo[['YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE', 'SECOND']])

# Filtering meteorological tide data for the lagoon period
df_meteo_filtered = df_meteo[df_meteo['DATE'].isin(df_lagoa['DATE'])]

# Merging both DataFrames using date as the key
df_merged = pd.merge(df_lagoa[['DATE', 'DADOS']], df_meteo_filtered[['DATE', 'avg_water_l1_ibge']], on='DATE', how='inner')

# Handling missing data
df_merged.dropna(inplace=True)

# Function to calculate Pearson correlation with lags
def pearson_correlation_with_lag(df, lag_max=100):
    correlations = []
    for lag in range(-lag_max, lag_max+1):
        df_shifted = df.copy()

        # Adjusting the tide field with the lag
        df_shifted['METEO_TIDE_SHIFTED'] = df_shifted['avg_water_l1_ibge'].shift(lag)

        # Calculating Pearson correlation between lagoon data and meteorological tide with lag
        correlation = df_shifted['DADOS'].corr(df_shifted['METEO_TIDE_SHIFTED'])
        correlations.append((lag, correlation))

    return correlations

# Calculating correlation for lags from -48 to 48 hours
correlations = pearson_correlation_with_lag(df_merged)

# Finding the best lag with the highest correlation
best_lag, best_correlation = max(correlations, key=lambda x: abs(x[1]))

print(f'Best lag: {best_lag} hours')
print(f'Pearson correlation coefficient: {best_correlation}')

# Plotting correlations for visualization
lags, corr_values = zip(*correlations)

plt.figure(figsize=(12, 6))
plt.plot(lags, corr_values, marker='o', color='b')
plt.axhline(y=0.5, color='r', linestyle='--', label='Reference (y = 0.5)')  # Red reference line
plt.title('Pearson Correlation for Different Lags', fontsize=14)
plt.xlabel('Lag (hours)', fontsize=12)
plt.ylabel('Pearson Correlation', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
