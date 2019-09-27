import re
import requests
from bs4 import BeautifulSoup
from time import sleep

url = "https://www.ricardoeletro.com.br/Loja/Audio/5669?p=1&Fabricante=&Filtros=&cor=&tamanho=&precode=&precoate=&ordenacao=&limit=&site_id="

page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

listaProdutos = soup.find_all('div', class_='nome-produto-vertical')
listaValores = soup.find_all('div', class_='valores')

cont = 0

for prod in listaProdutos:

    strProd = '%s\n%s' % (prod.text, listaValores[cont].text)
    cont += 1
    strProd = strProd.replace('por R$','\npor R$')
    strProd = strProd.replace('ou ','\nou ')

    parcelado = 0

    try:
        if strProd.index('x R$'):
            parcelado = 1
    except Exception as e:
        parcelado = 0

    if parcelado == 1:
        arrProd = strProd.split('\n')
        arrParcelado = arrProd[3].split('R$')

        filtro = re.compile('([0-9]+)')
        resp = filtro.findall(arrParcelado[1])
        strValorParcela = '%s.%s' % (resp[0],resp[1])
        valorParcela = float(strValorParcela)

        strQtdeParcela = filtro.findall(arrParcelado[0])
        parcelas = int(strQtdeParcela[0])

        valorTotalParcelado = parcelas * valorParcela
        strValorTotalParcelado = '%4.2f' % valorTotalParcelado

        strProd = '%s\nTotal Parcelado: R$ %s' % (strProd, strValorTotalParcelado)

    print(strProd)
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------\n\n")
    sleep(5)