# coding: utf-8

from apisRequest import Search
from strToken import tokensTeste
import json
import os
import time
import pprint

s = Search()
tks = tokensTeste()

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_cep(cep = "83602690"):

    url = "https://viacep.com.br/ws/%s/json/" % (cep)

    s.make_url(url)
    s.headers = {'Content-type':'application/json'}
    s.make_content('get')
    s.make_soup('html.parser')

    return json.loads(s.content.content.decode('utf-8'))

def send_post(message="Test"):
    s.make_url("http://localhost/test-python-request.php")
    s.params = {'come-of-python':message}
    s.headers = None
    myTry = s.make_content('post')

    if myTry == 1:
        return s.content.content
    else:
        return 0

def get_holidays():
    s.make_url("https://api.calendario.com.br/?json=true&token=%s&ano=2019&estado=PR&cidade=Campo_Largo" % (tks.tk_holiday))
    s.make_content('get')

    list_holidays = json.loads(s.content.content.decode('utf-8'))

    resume_list = []

    for holiday in list_holidays:
        resume_list.append(
                [holiday.get('name'),holiday.get('date')]
        )
    return resume_list

def statistics_names_by_ibge(name="Maria"):
    s.make_url("https://servicodados.ibge.gov.br/api/v2/censos/nomes/%s" % (name))
    s.headers = {'Content-type':'application/json'}
    s.make_content('get')

    data_statistics = json.loads(s.content.content.decode('utf-8'))

    return  data_statistics

cont = 0

while cont < 100:
    try:
        print("LIST OPTIONS:")

        print("[1] Function get_cep()")
        print("[2] Function send_post()")
        print("[3] Function get_holidays()")
        print("[4] statistics_names_by_ibge()")
        print("[0] Stop this code")

        option = int(input("What option do you wanna?"))
        return_function = None

        if option == 1:
            param = input("Enter with the cep:")
            return_function = get_cep(param)

        elif option == 2:
            param = input("Enter with the message:")
            return_function = send_post(param)

        elif option == 3:
            return_function = get_holidays()

        elif option == 4:
            param = input("Enter with the name:")
            return_function = statistics_names_by_ibge(param)

        elif option == 0:
            break
        else:
            break

        qtde_time = 3
        qtde_time = int(input("How much time do you wanna see the answer?"))

        bar = ""

        for i in range(qtde_time):
            bar += "\033[33;43m   \033[m"
            pp = pprint.PrettyPrinter()
            pp.pprint(return_function)
            print(bar)

            time.sleep(1)
            limpar()

        limpar()
    except Exception as e:
        print(e)
        continue

    cont += 1