# import requests

# url = "https://v1.hockey.api-sports.io//odds?season"

# payload={}
# headers = {
#   'x-rapidapi-key': '181b008f0f91004c17435e30ad18299b',
#   'x-rapidapi-host': 'v1.hockey.api-sports.io'
# }

# response = requests.request("GET", url, headers=headers, data=payload)
# "1300"
# pprint(response.text)
# with open(f"test.log", "w") as log_file:
#     pprint(response.text, log_file)


import http.client
from pprint import pprint

conn = http.client.HTTPSConnection("v1.hockey.api-sports.io")

headers = {
    'x-rapidapi-host': "v1.hockey.api-sports.io",
    'x-rapidapi-key': "181b008f0f91004c17435e30ad18299b"
    }

conn.request("GET", "/games?id=1", headers=headers)


# conn.request("GET", "/games?league=1&season=2023", headers=headers)

# conn.request("GET", "/odds?season=2024&league=261", headers=headers)

res = conn.getresponse()
data = res.read()
json = data.decode("utf-8")

pprint(json)

with open(f"games.log", "w") as log_file:
    pprint(json, log_file)