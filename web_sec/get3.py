import requests

header = {'X-Password': 'admin'} 
r = requests.get('http://web-03.challs.olicyber.it/flag', headers=header)
print(r.text)
