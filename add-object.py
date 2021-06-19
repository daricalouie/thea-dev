import requests
import json

# get map from Darica's testing space

g = requests.get('https://gather.town/api/getMap?spaceId=bLC4E96xZ4dVKnTF\\testing&apiKey=doa91a6eaEZV6r5P&mapId=empty-room-small-brick')
print('get: '+str(g.status_code))
data = g.json()

# get radio

for x in data["objects"]:
    # print (x)
    if x["_name"] == "Custom Radio":
        radio = x

# get Nomtanso map

g = requests.get('https://gather.town/api/getMap?apiKey=doa91a6eaEZV6r5P&mapId=custom-entrance&spaceId=lflNFA5Yj90eCOz6\\Nomtanso_Labs')
print('get: '+str(g.status_code))
data = g.json()

# add radio to Nomtanso map

data["objects"].append(radio)
print(json.dumps(data))

# update Nomtanso map

p = requests.post('https://gather.town/api/setMap', json={"apiKey": "doa91a6eaEZV6r5P", "spaceId": "lflNFA5Yj90eCOz6\\Nomtanso_Labs", "mapId": "custom-entrance", "mapContent": data })

if p.status_code != 200:
    print(str(p.status_code)+ ' '+p.reason)
else:
    print('success')
