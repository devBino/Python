# coding: utf-8

#Autor: Fernando Bino Machado
#Descrição: Exemplo básico Web Scraping
#Recolhe no máximo 2 termos para pesquisa
#Executa Pesquisa no Google
#Percorre os links resultantes
#Salva os links em um arquivo html


import requests
from bs4 import BeautifulSoup

#armazena as tags <a></a>
listaLinks=[];

#define url base
urlBase = "https://www.google.com/search?q="

#recebe os termos
termos = str(input("Digite até 2 termos para sua pesquisa:"))

#trata os termos limitando os
lisTermos = termos.split(' ')
lisTermosLimit = lisTermos[0:2]


#monta os parametros para pesquisa e define url final para pesquisa
params = "";

for termo in lisTermosLimit:
    params = "%s%s+" % (params,termo)

urlFinal = "%s%s" % (urlBase,params)

urlFinal = urlFinal[0:len(urlFinal) - 1]

#faz a busca
page = requests.get(urlFinal)
soup=BeautifulSoup(page.content,'html.parser')
links=soup.find_all('a')

#percorre os links resultantes da pesquisa filtrando conforme os termos recebidos
for link in links:
    urLink = link.get('href')
    txLink = link.text
    for termo in lisTermosLimit:
        semelhanca = txLink.count(termo)
        if semelhanca > 0:
            urPesquisa = "https://www.google.com%s" % urLink
            if urPesquisa not in listaLinks:
                tag = "<a href='%s' target='_blanck'>%s</a>" % (urPesquisa,txLink)
                listaLinks.append(tag)

#monta o html dos links
htmlLinks=""

for l in listaLinks:
    htmlLinks = "%s<hr>%s" % (htmlLinks,l)

#pega o html modelo
arq = open('template.txt','r')
htmlBase = arq.read()
arq.close()

#define htmlFinal
htmlFinal = htmlBase.replace('<!-- links -->', htmlLinks)

#salva html no diretório atual
arq = open("lista-links.html", "w")
arq.write(htmlFinal)
arq.close()

#finaliza com saudação
print("; ) Obrigado por testar esse pequeno script!!!")
print("Um documento lista-links.html foi salvo na mesma pasta onde esse script rodou!!!")
print("\n------------------------------------------------")


