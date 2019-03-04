# coding: utf-8

import requests
from bs4 import BeautifulSoup
import pymysql.cursors
from random import randint
import time

def geraConteudo():
    #armazena as expressões já salvas
    listaLinks=[];

    #lista de palavras para sortear
    palavras = [
        'titanic','agua','verão','chuva','acidente','tecnologia','programação',
        'tv','corrida','filme','galaxia','pessoas','faculdade','cursos','comida',
        'animais','cobra','leão','formigas','colonia','bando','elefante','manada',
        'grupo','futball'
    ]

    #sorteia as palavras e monta a os termos
    palavra1 = palavras[randint(0,len(palavras) - 1)]
    palavra2 = palavras[randint(0,len(palavras) - 1)]

    lisTermosLimit = [palavra1,palavra2]

    #monta os parametros para pesquisa e define url final para pesquisa
    params = "";

    #define url base
    urlBase = "https://www.google.com/search?q="

    for termo in lisTermosLimit:
        params = "%s%s+" % (params,termo)

    urlFinal = "%s%s" % (urlBase,params)

    urlFinal = urlFinal[0:len(urlFinal) - 1]

    #faz a busca
    page = requests.get(urlFinal)
    soup=BeautifulSoup(page.content,'html.parser')
    links=soup.find_all('a')

    #inicia conexão com banco
    connection = pymysql.connect(
        host='localhost',
        user='fer',
        password='fer',
        db='nodejs',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )

    #percorre os links e salva no banco
    for link in links:
        urLink = link.get('href')
        txLink = link.text

        if urLink != "" and txLink != "":
            for termo in lisTermosLimit:
                semelhanca = txLink.count(termo)
                if semelhanca > 0:
                    urPesquisa = "https://www.google.com%s" % urLink
                    if urPesquisa not in listaLinks:
                        tag = "<a href='%s' target='_blanck'>%s</a>" % (urPesquisa, txLink)
                        listaLinks.append(tag)
                        try:
                            with connection.cursor() as cursor:
                                sql = "insert into subjects (link,text) values (%s,%s)"
                                cursor.execute(sql, (urPesquisa,txLink))
                            connection.commit()
                        finally:
                            print('Link salvo com sucesso!!')

    #fecha a conexão
    connection.close()

cont = 0

while(cont < 100):
    geraConteudo()
    time.sleep(60)