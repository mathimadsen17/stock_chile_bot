from bs4 import BeautifulSoup
import datetime
from tinydb import TinyDB, Query
import urllib3
import xlsxwriter

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


total_added = 0


def make_soup(url):
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    return BeautifulSoup(r.data,'lxml')

def limpiar_disponibilidad(x):
    x = str(x.replace('<',''))
    x = str(x.replace('span class="ui-pdp-buybox__quantity__available">', ''))
    x = str(x.replace(')/span>', ''))
    x = str(x.replace('(',''))
    x = str(x.replace('[',''))
    x = str(x.replace(']',''))
    x = str(x.replace('disponibles', ''))
    return x

def disponibilidad_PS5_mercadolibre(url):
    soup = make_soup(url)
    result = soup.find_all('span',class_="andes-button__content")

    cantidad_disponible = soup.find_all('span', class_= 'ui-pdp-buybox__quantity__available')

    cantidad_disponible = str(cantidad_disponible)


    if len(result) > 0:
        print(f'HAY {limpiar_disponibilidad(cantidad_disponible)} UNIDADES DISPONIBLES DE PS5 CON LECTOR EN MERCADO LIBRE')
        
    else:
        print("NO HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN MERCADO LIBRE")
    


