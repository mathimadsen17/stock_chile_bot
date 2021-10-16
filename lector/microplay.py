from bs4 import BeautifulSoup
import datetime
from tinydb import TinyDB, Query
import urllib3
import xlsxwriter

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://www.microplay.cl/producto/consola-ps5-sony/'
total_added = 0


def make_soup(url):
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    return BeautifulSoup(r.data,'lxml')

def disponibilidad_PS5_microplay(url):
    soup = make_soup(url)
    result = soup.find_all('a',class_="btn btn-submit btn-agregar2 nuevo")

    if len(result) > 0:
        print("HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN MICROPLAY")

    else:
        print("NO HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN MICROPLAY")