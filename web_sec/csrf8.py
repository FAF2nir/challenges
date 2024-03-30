import requests

json = {"username":"admin", "password":"admin"}
s = requests.Session()
r = s.post('url1', json=json)

final_flag = ""

for i in range(4):
  csrftoken = r.json()['csrf']
  index = dict(index=i, csrf=csrftoken)

  r = s.get("url2", params=index)

  final_flag += r.json()['flag_piece']

print(final_flag)