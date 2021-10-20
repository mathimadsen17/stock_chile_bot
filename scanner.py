from bs4 import BeautifulSoup
import urllib3
import threading
from telegram import telegram_bot_sendtext


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Scanner:
    # def __init__(self, tienda, url, frecuencia=60, *soup_args, **soup_kwargs):
    def __init__(self, tienda, url, *soup_args, **soup_kwargs):
        self.tienda = tienda
        self.url = url
        self.frecuencia = 60
        self.soup_args = soup_args
        self.soup_kwargs = soup_kwargs
        self.disponibilidad = None
        self.hebra = None
        print(f"URL de {self.tienda}: {self.url}")
        print(f"Argumentos para Soup: {self.soup_args}, {self.soup_kwargs}")

    def revisa_disponibilidad(self):
        soup = self.make_soup(self.url)
        result = soup.find_all(*self.soup_args, **self.soup_kwargs)

        if len(result) > 0:
            print(f"Hay disponibilidad de PS5 en {self.tienda}: {self.url}")
            if self.disponibilidad is not True:
                self.disponibilidad = True
                print("Envío a Telegram.")
                # telegram_bot_sendtext(
                #     f"HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN FALABELLA {url}"
                # )
        else:
            print(f"No hay disponibilidad en {self.tienda}.")
            if self.disponibilidad is not False:
                self.disponibilidad = False
                print("Envio a Telegram.")

    @staticmethod
    def make_soup(url):
        http = urllib3.PoolManager()
        r = http.request("GET", url)
        return BeautifulSoup(r.data, "lxml")

    def inicia(self):
        self.detiene()
        self.revisa_disponibilidad()
        self.hebra = threading.Timer(self.frecuencia, self.inicia)
        self.hebra.start()

    def detiene(self):
        if self.hebra is not None and self.hebra.is_alive:
            self.hebra.cancel()
            print(f"[{self.tienda}] Detiene la hebra")


if __name__ == "__main__":
    url = "https://www.falabella.com/falabella-cl/product/15199827/Consola-Nintendo-Switch-Lite-Blue/15199827"
    args = ("button",)
    kw_args = {
        "class_": "jsx-2166277967 button button-mkp-primary button-mkp-primary-xtra-large"
    }
    # Scanner("1234", 1, 3, 4, 5, otro={"algo": ["a", "b", 5]})
    fala_check = Scanner("fala", url, *args, **kw_args)
    fala_check.revisa_disponibilidad()
    fala_check.inicia()
    fala_check.detiene()

    # soup = make_soup(url)
    # result = soup.find_all(*args, **kw_args)
