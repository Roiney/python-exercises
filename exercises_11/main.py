import pandas as pd

#importar a base de dados
tabelas_vendas = pd.read_excel('Vendas.xlsx')

#visualizar a base de dados
#pd.set_option('display.max_columns', None)

#print(tabelas_vendas[['ID Loja','Valor Final']])
#print(tabelas_vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum())

#faturamento por loja
faturamento = tabelas_vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum()

#quantidade produtos vendidos por loja
quantidade = tabelas_vendas[['ID Loja','Quantidade']].groupby('ID Loja').sum()

#tickt médio por produto em cada loja
tickt_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()


#enviar email por relatório
