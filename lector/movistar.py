from bs4 import BeautifulSoup
import datetime
from tinydb import TinyDB, Query
import urllib3
import xlsxwriter

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://catalogo.movistar.cl/fullprice/sony-consola-ps5-juego-spider-man-miles-morales-ps5.html'
total_added = 0


def make_soup(url):
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    return BeautifulSoup(r.data,'lxml')


def disponibilidad_PS5_movistar(url):
    soup = make_soup(url)
    print(soup)

    result = soup.find_all("button")
    print(result)

    if len(result) > 0:
        print("HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN MOVISTAR")

    else:
        print("NO HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN MOVISTAR")

disponibilidad_PS5_movistar(url)