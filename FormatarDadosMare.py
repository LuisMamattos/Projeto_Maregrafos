import pandas as pd
from datetime import datetime, timedelta

# Configuração inicial
data_inicial = datetime(2024, 5, 9, 3, 0, 0)  # Começa em 9 de maio de 2024 às 03:00
intervalo = timedelta(hours=1)  # Incremento de 1 hora

# Nome dos arquivos de entrada e saída
arquivo_entrada = "meteo.csv"  # Ou "astro.csv"
arquivo_saida = "meteo_formatado.csv"

# Ler os dados brutos
with open(arquivo_entrada, "r") as f:
    dados = [float(linha.strip()) for linha in f.readlines()]

# Criar as colunas de data e formatar os dados
linhas = []
data_atual = data_inicial
for valor in dados:
    linha = [
        data_atual.year, data_atual.month, data_atual.day,
        data_atual.hour, data_atual.minute, data_atual.second,
        valor
    ]
    linhas.append(linha)
    data_atual += intervalo  # Incrementa 1 hora

# Criar DataFrame
colunas = ["YEAR", "MONTH", "DAY", "HOUR", "MINUTE", "SECOND", "avg_water_l1_ibge"]
df = pd.DataFrame(linhas, columns=colunas)

# Salvar no novo CSV
df.to_csv(arquivo_saida, sep=';', index=False)

print(f"Arquivo salvo como {arquivo_saida}")
