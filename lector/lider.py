from bs4 import BeautifulSoup
import urllib3
#from telegram import telegram_bot_sendtext

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://www.lider.cl/catalogo/product/sku/1086920'
tinyurl = 'https://tinyurl.com/2675s3bp'

def make_soup(url):
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    return BeautifulSoup(r.data,'html.parser')


def disponibilidad_PS5_lider(url):
    soup = make_soup(url)

    result = str(soup)

    if str("InStock") in result:
        print("HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN LIDER")
        telegram_bot_sendtext(f"HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN LIDER {tinyurl}")

    else:
        print("NO HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN LIDER")
        

