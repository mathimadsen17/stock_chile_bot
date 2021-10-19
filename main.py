from lector.falabella import disponibilidad_PS5_falabella
from lector.lider import disponibilidad_PS5_lider
from lector.mercado_libre import disponibilidad_PS5_mercadolibre
from lector.microplay import disponibilidad_PS5_microplay
from lector.zmart import disponiblidad_PS5_zmart
from digitales.lapolar_digital import disponiblidad_PS5_digital_lapolar
from lector.sony import disponibilidad_PS5_sony
from lector.weplay import disponibilidad_PS5_weplay
from digitales.ripley_digital import disponibilidad_PS5_digital_ripley
from lector.pcfactory import disponibilidad_PS5_pcfactory
from digitales.pcfactory_digital import disponibilidad_PS5_digital_pcfactory
from time import sleep
from telegram import telegram_bot_sendtext
from telegram_checker import telegram_bot_sendtext_checker


while True:
    disponibilidad_PS5_falabella('https://www.falabella.com/falabella-cl/product/prod37699550/COMBO-PLAYSTATION-5-+-JGO-SPIDER-MAN/sku37700168')
    disponibilidad_PS5_lider('https://www.lider.cl/catalogo/product/sku/1000000000359')
    if disponibilidad_PS5_mercadolibre('https://articulo.mercadolibre.cl/MLC-613490868-playstation-5-ps5-estandar-spider-man-miles-morales-_JM') == True:
        telegram_bot_sendtext("HAY STOCK DISPONIBLE DE PS5 CON LECTOR EN MERCADO LIBRE https://articulo.mercadolibre.cl/MLC-613490868-playstation-5-ps5-estandar-spider-man-miles-morales-_JM")
    disponibilidad_PS5_microplay('https://www.microplay.cl/producto/consola-ps5-sony/')
    disponiblidad_PS5_zmart('https://www.zmart.cl/scripts/prodView.asp?idProduct=78812')
    disponibilidad_PS5_pcfactory('https://www.pcfactory.cl/producto/39192-sony-bundle-consola-playstation-5--juego-marvel-s-spider-man-miles-morales-ps5')
    disponibilidad_PS5_sony('https://store.sony.cl/playstation5/p')
    disponibilidad_PS5_weplay('https://www.weplay.cl/consola-playstation-5.html')
    disponiblidad_PS5_digital_lapolar('https://www.lapolar.cl/consola-sony-playstation-5-digital/23395657.html')
    disponibilidad_PS5_digital_ripley('https://simple.ripley.cl/consola-ps5-digital-edition-2000380458314p?color_80=blanco&s=o')
    disponibilidad_PS5_digital_pcfactory('https://www.pcfactory.cl/producto/42732-sony-consola-playstation-5-version-all-digital--3-meses-playstation-plus')
    telegram_bot_sendtext_checker("still alive")
    sleep(60)
    


