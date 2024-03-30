from bs4 import BeautifulSoup
import requests

r = requests.get("url")
soup = BeautifulSoup(r.text, 'html.parser')

visited = []

headers = soup.find_all("h1")
a_tags = soup.find_all("a")
links = []
found = False

for el in a_tags:
    if el.text:
        links.append(el['href'])

for link in links:
    if link not in visited:
        r = requests.get(f"url{link}")
        soup = BeautifulSoup(r.text, 'html.parser')
        headers = soup.find_all('h1')
        a_tags  = soup.find_all('a')

        for el in a_tags:
            if el not in links:
                links.append(el['href'])

        visited.append(link)

        for header in headers:
            if header.text.find("flag") != -1:
                print(header.text)
                found = True

        if found:
            break
