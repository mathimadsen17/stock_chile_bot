from bs4 import BeautifulSoup
from telegram import telegram_bot_sendtext
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://www.zmart.cl/scripts/prodView.asp?idProduct=78812'
total_added = 0


def make_soup(url):
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    return BeautifulSoup(r.data,'lxml')

def disponiblidad_PS5_zmart(url):
    soup = make_soup(url)
    result = soup.find_all('input',class_="comprar2015")

    if len(result) > 0:
        print("HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN ZMART")
        telegram_bot_sendtext(f"HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN ZMART {url}")

    else:
        print("NO HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN ZMART")