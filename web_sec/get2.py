from requests import get
id = {'id': 'flag'}
r = get('url', params=id)
print(r.text)