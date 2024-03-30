import requests
from bs4 import BeautifulSoup

page = requests.get("url")
soup = BeautifulSoup(page.text, 'html.parser')

print(soup.find_all('p'))