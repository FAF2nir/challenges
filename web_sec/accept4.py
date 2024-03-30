import requests

header1 = {'Accept': 'application/xml'}
header2 = {'Accept': 'application/json'}

r = requests.get('url1', headers=header1)
print(r.text)

r = requests.get('url2', headers=header2)
print(r.text)