import requests
from bs4 import BeautifulSoup, Comment

page = requests.get('url')
soup = BeautifulSoup(page.text, 'html.parser')

#Funcition that checks if the text is a Comment object
comments = soup.find_all(string=lambda text:isinstance(text, Comment))

for c in comments:
  print(c)