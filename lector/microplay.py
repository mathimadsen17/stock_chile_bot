from bs4 import BeautifulSoup
import urllib3
from telegram import telegram_bot_sendtext

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
        telegram_bot_sendtext(f"HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN MICROPLAY {url}")

    else:
        print("NO HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN MICROPLAY")
        telegram_bot_sendtext(f"NO HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN MICROPLAY {url}")