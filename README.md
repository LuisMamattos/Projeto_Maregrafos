# Projeto_Maregrafos

Análise da Influência da Maré no Nível da Lagoa dos Patos

Introdução

Este projeto tem como objetivo analisar a influência das variações de maré sobre o nível da Lagoa dos Patos, utilizando dados coletados por sensores de baixo custo e dados fornecidos pelo IBGE. A metodologia envolve a separação das componentes da maré (astronômica e meteorológica) e a aplicação de técnicas de análise de séries temporais para identificar correlações e defasagens temporais.

Estrutura do Projeto

dados/

dados3.xlsx - Dados do nível da Lagoa dos Patos coletados por sensores ultrassônicos de baixo custo.

astro_formatado.csv - Dados da maré astronômica fornecidos pelo IBGE.

meteo_formatado.csv - Dados da maré meteorológica estimados a partir de modelos e observações.

notebooks/

Contém notebooks para visualização, pré-processamento, cálculo de correlação e análise sazonal.

scripts/

Contém scripts auxiliares para processamento, análise e visualização dos dados.

Metodologia

Coleta de Dados

Os dados de nível da Lagoa dos Patos foram obtidos por sensores ultrassônicos instalados em locais estratégicos.

Os dados de maré astronômica foram extraídos de bancos de dados do IBGE.

A maré meteorológica foi estimada a partir da diferença entre os dados observados e a componente astronômica.

Pré-processamento

Remoção de outliers e tratamento de dados faltantes.

Normalização das séries temporais para comparação adequada.

Cálculo da Correlação

Utilização da correlação de Pearson para medir a relação entre a maré e o nível da lagoa.

Variação do lag (atraso temporal) para identificar a defasagem com maior influência.

Análise Sazonal

Decomposição das séries utilizando STL e EMD para separar componentes de tendência, sazonalidade e ruído.

Tecnologias Utilizadas

Linguagens: Python

Bibliotecas Principais: Pandas, NumPy, SciPy, Matplotlib, Seaborn, Statsmodels

Ferramentas: Jupyter Notebook, MySQL (opcional para armazenamento de dados)
