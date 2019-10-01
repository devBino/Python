import re
import requests
from bs4 import BeautifulSoup
from time import sleep
import smtplib
from email.mime.text import MIMEText

#lista dos sites onde vai pesquisar
sites = [
    {
        'urlRaiz':'https://carros.mercadolivre.com.br/antigos/volkswagen/passat-antigo-3-porta',
        'configs':{
            'img':'lazy-load',
            'elem-ano':'div',
            'ano':'item__attrs',
            'local':'item__location',
            'elem-local':'div',
            'link':'item-link',
            'portas':'specs-item',
            'elem-portas':'li'
        }
    },
    {
        'urlRaiz':'https://www.olx.com.br/autos-e-pecas?q=passat%20antigo',
        'configs':{
            'img':'image',
            'ano':'OLXad-list-title',
            'elem-ano':'h2',
            'local':'detail-region',
            'elem-local':'p',
            'link':'OLXad-list-link',
            'portas':'sc-gqjmRU',
            'elem-portas':'dd'
        }
    }
]
#==================================================================
def enviaEmail(msg):
    smtp_ssl_host = 'smtp.gmail.com'
    smtp_ssl_port = 465

    username = 'programe2machado@gmail.com'
    password = '##'

    from_addr = 'programe2machado@gmail.com'
    to_addrs = ['fernando.bino.machado@gmail.com','edineibino09@gmail.com']

    message = MIMEText(msg, 'html')
    message['subject'] = 'Passat'
    message['from'] = from_addr
    message['to'] = ', '.join(to_addrs)

    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)

    server.login(username, password)
    server.sendmail(from_addr, to_addrs, message.as_string())
    server.quit()

    print(msg)
    sleep(2)
#==================================================================


#percorre os sites
for site in sites:
    pageSite = requests.get(site.get('urlRaiz'))
    soupSite = BeautifulSoup(pageSite.content,'html.parser')

    configs = site.get('configs')

    imgs = soupSite.find_all('img',class_=configs.get('img'))
    anos = soupSite.find_all(configs.get('elem-ano'),class_=configs.get('ano'))
    locais = soupSite.find_all(configs.get('elem-local'),class_=configs.get('local'))
    links = soupSite.find_all('a', class_=configs.get('link'))

    cont = 0

    for link in links:
        txtAno = anos[cont].text
        try:
            if txtAno.index('1977') or txtAno.index('1978'):

                page = requests.get(link.get('href'))
                soup = BeautifulSoup(page.content, 'html.parser')
                portas = soup.find_all(configs.get('elem-portas'), class_=configs.get('portas'))

                qtdePortas = ''

                for porta in portas:
                    strPorta = str(porta.text)

                    if strPorta.lower().index('portas') and strPorta.lower().index('3'):
                        qtdePortas = 3

                        msgLink = link.get('href')
                        msgLocal = locais[cont].text
                        ancora = '<a href="%s">%s - Clique para Ver</a>' % (msgLink,msgLocal)

                        msg = '<html><head></head><body>Foi Localizado um Passat em <br> %s </body></html>' % ancora

                        enviaEmail(msg)

        except Exception as e:
            pass
        cont += 1