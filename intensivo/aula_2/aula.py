import pandas as pd

tabela = pd.read_csv("telecom_users.csv")

# Passo 2: Visualizar a base de dados
# excluido a coluna Unnamed: 0 -> drop precisa do nome e do eixo -> eixo = 0 é linha, eixo =1 é coluna

tabela = tabela.drop("Unnamed: 0", axis=1)
print(tabela.info())

# - Valores que estão reconhecidos de forma errada -> to_numeric transforma em float a coluna "TotalGasto" e errors trata erros de texto 
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
print(tabela.info())

#resolvendo valores vazios
# deletando as colunas que tem TODAS colunas vazias 
# axis = 0 _> linha ou axis = 1 _> coluna
tabela = tabela.dropna(how="all", axis=1)
# deletando as linhas que possuem ALGUM VALORES VAZIOS
tabela = tabela.dropna(how="any", axis=0)

print(tabela.info())


#analise inicial 
#contar os valores da coluna Churn
print(tabela["Churn"].value_counts())
#Porcentagem da contagem
print(tabela["Churn"].value_counts(normalize=True))
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

import plotly.express as px

grafico = px.histogram(tabela, x="FaturaDigital", color="Churn", text_auto=True,  histnorm='percent')
grafico.show()

# etapa 1: criar o gráfico
# for coluna in tabela.columns:
#     # para edições nos gráficos: https://plotly.com/python/histograms/
#     # para mudar a cor do gráfico , color_discrete_sequence=["blue", "green"]
#     grafico = px.histogram(tabela, x="FaturaDigital", color="Churn", text_auto=True,  histnorm='probability density')
#     # etapa 2: exibir o gráfico
#     grafico.show()
