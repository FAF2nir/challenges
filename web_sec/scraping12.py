import requests
from bs4 import BeautifulSoup

def get_source(tag, soup):
  sources = []
  for i in soup.find_all(tag):
    if tag == 'tag' or tag == 'script' or tag == 'video' or tag == 'audio' or tag == 'iframe' or tag == 'embed' or tag == 'source':
      sources.append(i.get('src'))
    elif tag == 'link':
      sources.append(i.get('href'))
    elif tag == 'object':
      sources.append(i.get('data'))
  
  return sources

r = requests.get("url")
soup = BeautifulSoup(r.text, 'html.parser')

css_list = get_source('link', soup) #for the css
js_list = get_source('script', soup) #for the js

for i in css_list:
  r = requests.get(f"url{i}")
  soup = BeautifulSoup(r.text, 'html.parser')
  print(soup.text.find('flag'))

for i in js_list:
  r = requests.get(f'url{i}')
  soup = BeautifulSoup(r.text, 'html.parser')
  print(soup.text.find('flag'))
  print(soup.text)