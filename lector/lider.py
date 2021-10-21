from bs4 import BeautifulSoup
import urllib3
from telegram import telegram_bot_sendtext

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://www.lider.cl/catalogo/product/sku/982101'
tinyurl = 'https://tinyurl.com/2nzzjb4a'

def make_soup(url):
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    return BeautifulSoup(r.data,'html.parser')


def disponibilidad_PS5_lider(url):
    soup = make_soup(url)

    result = soup.find_all(class_="row")

    if len(result) > 0:
        print("HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN LIDER")
        telegram_bot_sendtext(f"HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN LIDER {tinyurl}")

    else:
        print("NO HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN LIDER")
        


