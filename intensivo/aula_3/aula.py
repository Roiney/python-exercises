from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

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