import requests
from bs4 import BeautifulSoup

page = requests.get('url')
soup = BeautifulSoup(page.text, 'html.parser')

#this generates a list of html elements
all_letters = soup.find_all('span')

final_flag = "flag{"

for i in all_letters:
  final_flag += i.get_text()

print(final_flag + '}')