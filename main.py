from lector.falabella import disponibilidad_PS5_falabella
from lector.lider import disponibilidad_PS5_lider
from lector.mercado_libre import disponibilidad_PS5_mercadolibre
from lector.microplay import disponibilidad_PS5_microplay
from lector.ripley import disponibilidad_PS5_ripley
from lector.zmart import disponiblidad_PS5_zmart
from lector.lider_juego import disponibilidad_PS5_lider_juego
from digitales.lapolar_digital import disponiblidad_PS5_digital_lapolar
from lector.sony import disponibilidad_PS5_sony
from lector.weplay import disponibilidad_PS5_weplay
from digitales.ripley_digital import disponibilidad_PS5_digital_ripley
from lector.pcfactory import disponibilidad_PS5_pcfactory
from digitales.pcfactory_digital import disponibilidad_PS5_digital_pcfactory
from time import sleep
from telegram_checker import telegram_bot_sendtext_checker
import datos

while True:
    disponibilidad_PS5_falabella(datos.link_falabella_lector)
    disponibilidad_PS5_falabella(datos.link_falabella_lecto_juego)
    disponibilidad_PS5_mercadolibre(datos.link_mercado_libre_lector) 
    #disponibilidad_PS5_lider_juego(datos.link_lider_lector_juego)
    #disponibilidad_PS5_lider(datos.link_lider_lector)
    disponibilidad_PS5_microplay(datos.link_microplay_lector)
    disponiblidad_PS5_zmart(datos.link_zmart_lector)
    disponibilidad_PS5_pcfactory(datos.link_pcfactory_lector)
    disponibilidad_PS5_ripley(datos.link_ripley_lector)
    disponibilidad_PS5_sony(datos.link_sony_lector)
    disponibilidad_PS5_weplay(datos.link_weplay_lector)
    disponiblidad_PS5_digital_lapolar(datos.link_lapolar_digital)
    disponibilidad_PS5_digital_ripley(datos.link_ripley_digital)
    disponibilidad_PS5_digital_pcfactory(datos.link_pcfactory_digital)
    telegram_bot_sendtext_checker("still alive")
    sleep(300)
    


