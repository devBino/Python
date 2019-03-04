#Autor: Fernando Bino Machado
#Descrição: Exemplo básico Requisições em Python
#Executa o script enquanto a opção continuar for igual a 1
#Captura e valida o cep digitado
#Faz a requisição a API viacep
#Armazena em lista
#Salva em arquivo txt

import os
import json
import requests

#armazena dicionarios dos ceps que serão pesquisados
listaCeps = []

#monta a chamada para o programa
def montagem(continuar):
    try:
        #se é pra continuar recolhe o cep, trata pesquisa e armazena na listaCeps[]
        if continuar == 1:
            # Capturando o cep do usuário
            cep = int(input("Digite o cep desejado: "))

            if len(str(cep)) == 8:
                # monta url para requisição
                url = 'https://viacep.com.br/ws/%s/json/' % cep

                # define os cabeçarios
                headers = {'Content-Type': 'application/json'}

                # captura os dados
                response = requests.get(url, headers)

                dadosResposta = json.loads(response.content.decode('utf-8'))

                listaCeps.append(
                    {
                        'cep': cep, 'dados': dadosResposta
                    }
                )
            else:
                print("Cep informado inválido")
                limpar()
        else:
        #se não é pra continuar
            #salva os ceps
            arq = open("lista-ceps.txt", "w")
            arq.write(str(listaCeps))
            arq.close()

            #finaliza com saudação
            print("; ) Obrigado por testar esse pequeno script!!!")
            print("Um documento lista-ceps.txt foi salvo na mesma pasta onde esse script rodou!!!")
            print("\n------------------------------------------------")
            
            limpar()
    except Exception as e:
        print(e)
        limpar()
#-----------------------------------------------------------------------

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')
#-----------------------------------------------------------------------

#inicio do script
continuar = 1
qtde=0

while continuar == 1:
    if continuar == 1:
        if qtde > 0:
            continuar = int(input("Deseja Continuar? Digite [1] Sim [0] Não"))
            print("\n-----------------------------------------------------------------------------")

        montagem(continuar)
    else:
        continue
    qtde += 1
    limpar()