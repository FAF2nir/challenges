import requests

s = requests.Session()
s.get('url1')

r = s.get('url2')
print(r.text)
