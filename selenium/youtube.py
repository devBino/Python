# coding: utf-8

from selenium import webdriver
import time

listaVideosFinal=[]

#informe manualmente uma lista de urls de videos, mas isso poderia vir de um banco de dados por exemplo
def listaVideos():
    listaDeVideos = [
        'https://www.youtube.com/watch?v=Nd7PMibKsZE',
        'https://www.youtube.com/watch?v=aa342sjXn9A',
        'https://www.youtube.com/watch?v=p53F_BI0BTE',
        'https://www.youtube.com/watch?v=IVhBe6tV0tA',
        'https://www.youtube.com/watch?v=i50ZAs7v9es',
        'https://www.youtube.com/watch?v=2dJpvYYnSms',
        'https://www.youtube.com/watch?v=tLfWKHlzie4',
        'https://www.youtube.com/watch?v=2T-vE_StCdg',
        'https://www.youtube.com/watch?v=YlsQ6hjSZ8A'
    ]

    return listaDeVideos
#=======================================================
def setTempo(tempoInicial):
    horas = 0
    minutos = 0
    segundos = 0

    # tratando a maior parte dos casos em que string tempo possa vir do youtube
    if len(tempoInicial) == 4:
        minutos = tempoInicial[0:1]
        segundos = tempoInicial[2:4]

    elif len(tempoInicial) == 5:
        minutos = tempoInicial[0:2]
        segundos = tempoInicial[3:5]

    elif len(tempoInicial) == 7:
        horas = tempoInicial[0:1]
        minutos = tempoInicial[2:4]
        segundos = tempoInicial[5:8]

    elif len(tempoInicial) == 8:
        horas = tempoInicial[0:2]
        minutos = tempoInicial[3:5]
        segundos = tempoInicial[6:9]

    tempoFinal = (int(horas) * 3600) + (int(minutos) * 60) + int(segundos)

    return tempoFinal
#=======================================================

#percorre os videos acionando selenium e pegando informações do titulo e tempo do video
def percorreVideos():

    firefox = webdriver.Firefox()

    for link in listaVideos():

        try:
            firefox.get(link)

            tempo = firefox.find_element_by_class_name('ytp-time-duration').text
            titulo = firefox.find_element_by_class_name('ytd-video-primary-info-renderer').text

            time.sleep(3)

            infoTitulo = "Titulo Video: %s\n" % (titulo)
            infoTempo = "Tempo Video: %s"  % (tempo)

            print(infoTitulo)
            print(infoTempo)
            print(">> Executando...")
            print("_______________________________________________________________________________________________________")

            if tempo != None and tempo != "":
                tempoVideo = setTempo(tempo)
                time.sleep(tempoVideo)
            else:
                continue
        except Exception as erro:
            print("Ocorreu um erro ao tentar executar a url...")
            continue

    firefox.close()


percorreVideos()
