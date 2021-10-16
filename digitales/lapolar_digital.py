from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://www.lapolar.cl/consola-sony-playstation-5-digital/23395657.html'

def make_soup(url):
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    return BeautifulSoup(r.data,'lxml')

def disponiblidad_PS5_digital_lapolar(url):
    soup = make_soup(url)
    result = soup.find_all('button',class_="add-to-cart lp-button lp-button--medium lp-button--inverted lp-button--borderless lp-button--no-hover lp-font--uppercase lp-font--barlow ms-full-width")
    result = str(result)
    if str("Agregar a la Bolsa") in result:
        print("HAY STOCK DISPONIBLE DE PS5 DIGITAL EN LA POLAR")

    else:
        print("NO HAY STOCK DISPONIBLE DE PS5 DIGITAL EN LA POLAR")
        
