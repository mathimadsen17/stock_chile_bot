from bs4 import BeautifulSoup
import requests
import urllib3
from telegram import telegram_bot_sendtext


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://www.pcfactory.cl/producto/42732-sony-consola-playstation-5-version-all-digital--3-meses-playstation-plus'
total_added = 0


def make_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text,'lxml')

def disponibilidad_PS5_digital_pcfactory(url):
    soup = make_soup(url)
    result = soup.find(class_='product-single__add-to-cart-button')
    result = str(result)

    if str("Añadir al carro") in result:
        print("HAY STOCK DISPONIBLE DE PS5 DIGITAL EN PC FACTORY")
        telegram_bot_sendtext(f"HAY STOCK DISPONIBLE DE PS5 DIGITAL EN PC FACTORY {url}")

    else:
        print("NO HAY STOCK DISPONIBLE DE PS5 DIGITAL EN PC FACTORY")
        telegram_bot_sendtext(f"NO HAY STOCK DISPONIBLE DE PS5 DIGITAL EN PC FACTORY {url}") 
