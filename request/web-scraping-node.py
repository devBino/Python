import requests
from bs4 import BeautifulSoup
from random import randint
import time

def key_words():
    # some words in list
    list_words = [
        'titanic', 'agua', 'verão', 'chuva', 'acidente', 'tecnologia', 'programação',
        'tv', 'corrida', 'filme', 'galaxia', 'pessoas', 'faculdade', 'cursos', 'comida',
        'animais', 'cobra', 'leão', 'formigas', 'colonia', 'bando', 'elefante', 'manada',
        'grupo', 'futball'
    ]

    return list_words
#====================================================

def make_web_scraping(expression):

    #define the url to search
    urlBase = "https://www.google.com.br/search?q="
    words = expression.split(',')

    params = ""

    for word in words:
        params = "%s+%s" % (params,word)

    urlFinal = "%s%s" % (urlBase,params)

    #make the web scraping
    page = requests.get(urlFinal)

    validate_links(BeautifulSoup(page.content,'html.parser'),words)

#====================================================
def validate_links(content,words):
    links = content.find_all('a')
    list_links = []
    expression =  "%s,%s" % (words[0],words[1])

    for link in links:
        href_link = link.get('href')

        if link.text.count(words[0]) > 0 or link.text.count(words[1]) > 0:

            urPesquisa = "https://www.google.com%s" % href_link

            link_info = {
                'token':'##','title': link.text,'link':urPesquisa,'words':expression
            }

            send_link_node(link_info)
#====================================================
def send_link_node(params):
    url = "http://localhost:3000/insert-new-web-scraping"

    response = requests.post(url=url,data=params)

    print(response.content)
#====================================================
def run_script():
    list_words = key_words()

    cont = 0

    while cont < 1000:
        # choose the words between list_words
        word_one = list_words[randint(0, len(list_words) - 1)]
        word_two = list_words[randint(0, len(list_words) - 1)]

        expression = "%s,%s" % (word_one, word_two)

        make_web_scraping(expression)
        cont += 1
        time.sleep(15)
# ====================================================

run_script()