import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados de direção do vento e nível da lagoa
df_vento = pd.read_csv('dados_vento_filtrado.csv', sep=';')
df_lagoa = pd.read_csv('dados_resampled.csv', sep=';')

# Converter as colunas de data e hora para datetime
df_vento['DataHora'] = pd.to_datetime(df_vento['DataHora'])
df_lagoa['DATE'] = pd.to_datetime(df_lagoa[['YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE', 'SECOND']])

# Filtrar os dados de vento para o mesmo período da Lagoa dos Patos
df_vento_filtered = df_vento[df_vento['DataHora'].isin(df_lagoa['DATE'])]

# Mesclar os dois DataFrames pelo campo DataHora/DATE
df_merged = pd.merge(df_lagoa[['DATE', 'DADOS']], df_vento_filtered[['DataHora', 'Mediana Direção Vento']], left_on='DATE', right_on='DataHora', how='inner')

# Tratar dados faltantes (caso haja)
df_merged.dropna(inplace=True)

# Garantir que os dados numéricos sejam tratados corretamente (substituir vírgulas por pontos e converter para float)
df_merged['DADOS'] = df_merged['DADOS'].apply(lambda x: float(str(x).replace(',', '.')))
df_merged['Mediana Direção Vento'] = df_merged['Mediana Direção Vento'].apply(lambda x: float(str(x).replace(',', '.')))

# Função para calcular a correlação de Pearson com diferentes lags
def pearson_correlation_with_lag(df, lag_max=100):
    correlations = []
    for lag in range(-lag_max, lag_max+1):
        df_shifted = df.copy()

        # Ajustar a direção do vento com o lag
        df_shifted['VENTO_SHIFTED'] = df_shifted['Mediana Direção Vento'].shift(lag)

        # Calcular a correlação de Pearson entre o nível da lagoa e a direção do vento com o lag
        correlation = df_shifted['DADOS'].corr(df_shifted['VENTO_SHIFTED'])
        correlations.append((lag, correlation))

    return correlations

# Calcular correlação para lags de -48 a 48 horas
correlations = pearson_correlation_with_lag(df_merged)

# Encontrar o melhor lag com a maior correlação
best_lag, best_correlation = max(correlations, key=lambda x: abs(x[1]))

print(f'Melhor lag: {best_lag} horas')
print(f'Coeficiente de correlação de Pearson: {best_correlation}')

# Plotar as correlações para visualização
lags, corr_values = zip(*correlations)

plt.figure(figsize=(12, 6))
plt.plot(lags, corr_values, marker='o', markersize=1, color='b')
plt.axhline(y=0.5, color='r', linestyle='--', label='Referência (y = 0.5)')  # Linha de referência
plt.title('Correlação de Pearson para Diferentes Lags', fontsize=14)
plt.xlabel('Lag (horas)', fontsize=12)
plt.ylabel('Correlação de Pearson', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
