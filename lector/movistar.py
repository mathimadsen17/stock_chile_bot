from bs4 import BeautifulSoup
import requests
import urllib3
from telegram import telegram_bot_sendtext


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://catalogo.movistar.cl/fullprice/sony-control-inalambrico-dualsense.html'
total_added = 0


def make_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text,'html.parser')

def disponibilidad_PS5_movistar(url):
    soup = make_soup(url)
    result = soup.find_all(id="buy-button")
    result = str(result)
    print(soup)

    if str("Agregar a la bolsa") in result:
        print("HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN MOVISTAR")
        

    else:
        print("NO HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN MOVISTAR")

disponibilidad_PS5_movistar(url)
