from bs4 import BeautifulSoup
import urllib3
from telegram import telegram_bot_sendtext

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://www.weplay.cl/consola-playstation-5.html'
total_added = 0


def make_soup(url):
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    return BeautifulSoup(r.data,'lxml')

def disponibilidad_PS5_weplay(url):
    soup = make_soup(url)
    result = soup.find_all(class_="action primary tocart")

    if len(result) > 0:
        print("HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN WEPLAY")
        telegram_bot_sendtext(f"HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN WEPLAY {url}")

    else:
        print("NO HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN WEPLAY")
        
