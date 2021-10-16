import requests
from bs4 import BeautifulSoup

my_url= 'https://simple.ripley.cl/samsung-galaxy-s21-128gb-phantom-black-2000382234695p?color_80=negro&s=o'
response = requests.get(my_url)
soup = BeautifulSoup(response.text, "lxml")
result = soup.find(id="buy-button")
print(result)