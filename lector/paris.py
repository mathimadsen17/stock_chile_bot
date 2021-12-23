from bs4 import BeautifulSoup
import requests
import urllib3
#from telegram import telegram_bot_sendtext


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://www.paris.cl/consola-ps5-440437999.html'
total_added = 0


def make_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text,'lxml')

def disponibilidad_PS5_paris(url):
    soup = make_soup(url)
    result = soup.find()
    result = str(result)

    

    if str("ecommerce") in result:
        print("HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN PARIS")
        #telegram_bot_sendtext(f"HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN PARIS {url}")

    else:
        print("NO HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN PARIS")    
disponibilidad_PS5_paris(url)