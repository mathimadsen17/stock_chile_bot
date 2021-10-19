from bs4 import BeautifulSoup
import requests
import urllib3
from telegram import telegram_bot_sendtext


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://simple.ripley.cl/consola-ps5-digital-edition-2000380458314p?color_80=blanco&s=o'
total_added = 0


def make_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text,'lxml')

def disponibilidad_PS5_digital_ripley(url):
    soup = make_soup(url)
    result = soup.find_all(id="buy-button")
    result = str(result)

    if str("Agregar a la bolsa") in result:
        print("HAY STOCK DISPONIBLE DE PS5 DIGITAL EN RIPLEY")
        telegram_bot_sendtext(f"HAY STOCK DISPONIBLE DE PS5 DIGITAL EN RIPLEY {url}")

    else:
        print("NO HAY STOCK DISPONIBLE DE PS5 DIGITAL EN RIPLEY")
