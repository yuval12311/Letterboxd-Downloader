import string

import requests
from bs4 import BeautifulSoup

def imdb_id(LB_URL: string):
    return imdb_id_from_URL(imdb_URL_from_LB(LB_URL))

def imdb_URL_from_LB(LB_URL: string):
    page = requests.get(LB_URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find("a", string="IMDb")
    return result["href"]

def imdb_id_from_URL(URL: string):
    return URL.split('/')[4]



