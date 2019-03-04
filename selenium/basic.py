from selenium import webdriver
from random import randint
from time import sleep

firefox = webdriver.Firefox()

url = 'https://www.globo.com/'

firefox.get(url)

listaLinks = []

for link in firefox.find_elements_by_xpath('//a[@href]'):
    listaLinks.append(link.get_attribute('href'))

linkSorteado = listaLinks[randint(0, len(listaLinks)-1)]

firefox.get(linkSorteado)

sleep(10)

firefox.close()