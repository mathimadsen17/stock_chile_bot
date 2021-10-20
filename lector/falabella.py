from bs4 import BeautifulSoup
import urllib3
from telegram import telegram_bot_sendtext


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://www.falabella.com/falabella-cl/product/15199827/Consola-Nintendo-Switch-Lite-Blue/15199827"
total_added = 0


def make_soup(url):
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    return BeautifulSoup(r.data, "lxml")


def disponibilidad_PS5_falabella(url):
    soup = make_soup(url)
    result = soup.find_all(
        "button",
        class_="jsx-2166277967 button button-mkp-primary button-mkp-primary-xtra-large",
    )

    if len(result) > 0:
        print("HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN FALABELLA")
        telegram_bot_sendtext(
            f"HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN FALABELLA {url}"
        )

    else:
        print("NO HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN FALABELLA")
