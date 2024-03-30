import requests

cookie = dict(password='admin')

r = requests.get('url', cookies=cookie)
print(r.text)