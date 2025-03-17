import pandas as pd

# Lendo o arquivo Excel
df = pd.read_excel('dados3.xlsx')  # Substitua pelo nome correto do arquivo

# Convertendo a coluna 'created_at' para o formato de data/hora
df['created_at'] = pd.to_datetime(df['created_at'])

# Definindo 'created_at' como índice para o resample
df.set_index('created_at', inplace=True)

# Definindo o intervalo de datas (substitua com as datas desejadas)
data_inicial = '2024-05-01'  # Data inicial
data_final = '2024-06-20'    # Data final

# Filtrando os dados pelo intervalo de datas
df_filtered = df[(df.index >= data_inicial) & (df.index <= data_final)]

# Resample: Calculando a mediana a cada 1 hora
df_resampled = df_filtered.resample('1h').median()

# Extraindo as partes da data e hora
df_resampled['YEAR'] = df_resampled.index.year
df_resampled['MONTH'] = df_resampled.index.month
df_resampled['DAY'] = df_resampled.index.day
df_resampled['HOUR'] = df_resampled.index.hour
df_resampled['MINUTE'] = df_resampled.index.minute
df_resampled['SECOND'] = df_resampled.index.second

# Criando o arquivo CSV no formato desejado
df_resampled = df_resampled[['YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE', 'SECOND', 'field1']]
df_resampled.rename(columns={'field1': 'DADOS'}, inplace=True)

# Salvando os dados no arquivo CSV
df_resampled.to_csv('dados_resampled.csv', sep=';', index=False)

print("Arquivo CSV gerado com sucesso!")
