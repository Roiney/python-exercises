import pandas as pd

tabela = pd.read_csv("telecom_users.csv")

# Passo 2: Visualizar a base de dados
# excluido a coluna Unnamed: 0 -> drop precisa do nome e do eixo -> eixo = 0 é linha, eixo =1 é coluna

tabela = tabela.drop("Unnamed: 0", axis=1)
print(tabela)