from selenium import webdriver
import time

navegador = webdriver.Chrome()
navegador.get('https://www.google.com/')


#buscando campo de busca e digitando
navegador.find_element('xpath', \
'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dolar")

#dando enter
navegador.find_element('xpath', \
'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("")

time.sleep(15)