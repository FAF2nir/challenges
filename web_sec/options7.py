import requests

r = requests.options('url')

r = requests.put('url')
print(r.headers)