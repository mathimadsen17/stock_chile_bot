from bs4 import BeautifulSoup
import urllib3
from telegram import telegram_bot_sendtext

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://store.sony.cl/playstation5/p'
total_added = 0


def make_soup(url):
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    return BeautifulSoup(r.data,'lxml')

def disponibilidad_PS5_sony(url):
    soup = make_soup(url)
    result = soup.find_all(class_="box buy")
    result = str(result)
    
    if str('Selecione') in result:
        print("HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN SONY")
        telegram_bot_sendtext(f"HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN SONY {url}")

    else:
        print("NO HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN SONY")
        telegram_bot_sendtext(f"NO HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN SONY {url}")

