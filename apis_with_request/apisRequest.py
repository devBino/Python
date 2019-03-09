import requests
from bs4 import BeautifulSoup

class Search:
    def __init__(self,strUrl=None):
        self.url = None
        self.content = None
        self.soup = None
        self.headers = None
        self.params = None

    def make_url(self,strUrl=None):
        self.url = strUrl

    def make_content(self, tp='get'):
        try:
            if self.headers != None:
                if tp == 'get':
                    self.content = requests.get(self.url,self.headers)
                    return 1
                elif tp == 'post':
                    if self.params != None:
                        self.content = requests.post(url=self.url,data=self.params)
                        return 1
                    else:
                        print("Need define params in make_content function\n")
                        return 0
            else:
                if tp == 'get':
                    self.content = requests.get(self.url)
                    return 1
                elif tp == 'post':
                    if self.params != None:
                        self.content = requests.post(url=self.url, data=self.params)
                        return 1
                    else:
                        print("Need define params in make_content function\n")
                        return 0
        except Exception as e:
            print("You have a error in make_content")
            return 0


    def make_soup(self,opt_parser):
        self.soup = BeautifulSoup(self.content.content,opt_parser)