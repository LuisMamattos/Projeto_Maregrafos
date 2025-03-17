import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo CSV
df = pd.read_csv('astro_formatado.csv', sep=';')

# Criando uma coluna de timestamp com base em todas as colunas de data e hora
df['Timestamp'] = pd.to_datetime(df[['YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE', 'SECOND']])

# Ordenando os dados por timestamp (caso não estejam)
df = df.sort_values('Timestamp')

# Plotando o gráfico com pontos menores
plt.figure(figsize=(12, 6))
plt.plot(df['Timestamp'], df['avg_water_l1_ibge'], marker='o', markersize=0, color='b', label='Average Water Level')

# Configurações do gráfico
plt.title('Variation of Astronomical tide Level Over Time', fontsize=14)
plt.xlabel('Time', fontsize=12)
plt.ylabel('Level', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

# Exibindo o gráfico
plt.show()
