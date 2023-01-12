from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

navegador = webdriver.Chrome()
navegador.get('https://www.google.com/')


#buscando campo de busca e digitando
navegador.find_element('xpath', \
'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dolar")

#dando enter
navegador.find_element('xpath', \
'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

#pegando a cotação
cotacao_dolar = navegador.find_element('xpath', \
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').\
    get_attribute("data-value")

print(cotacao_dolar)

#buscando campo de busca e digitando
navegador.get('https://www.google.com/')


#buscando campo de busca e digitando
navegador.find_element('xpath', \
'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")

#dando enter
navegador.find_element('xpath', \
'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

#pegando a cotação
cotacao_euro = navegador.find_element('xpath', \
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').\
    get_attribute("data-value")

print(cotacao_euro)


# #buscando campo de busca e digitando
navegador.get('https://www.melhorcambio.com/ouro-hoje')


# #pegando a cotação
cotacao_ouro = navegador.find_element('xpath', \
     '//*[@id="comercial"]').\
     get_attribute("value")

cotacao_ouro = cotacao_ouro.replace(',', '.')

print(cotacao_ouro)


#trabalhando com o pandas

tabela = pd.read_excel('Produtos.xlsx')

tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)

# atualizar o preço base reais (preço base original * cotação)
tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]

# atualizar o preço final (preço base reais * Margem)
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

tabela["Preço de Venda"] = tabela["Preço de Venda"].map("R${:.2f}".format)
tabela.to_excel('Produtos_novo.xlsx', index=False)

print(tabela)