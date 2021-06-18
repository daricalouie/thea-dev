import requests
import json

g = requests.get('https://gather.town/api/getMap?spaceId=bLC4E96xZ4dVKnTF\\testing&apiKey=doa91a6eaEZV6r5P&mapId=empty-room-small-brick')
print('get: '+str(g.status_code))
data = g.json()
for x in data["objects"]:
    # print (x)
    if x["_name"] == "Fire Pit (Lit)":
        print(x["sound"]["src"])
        x["sound"]["src"] = "https://github.com/daricalouie/TillinghastOrganization/raw/gh-pages/img/static.mp3"
        # x["sound"]["src"] = "https://github.com/daricalouie/TillinghastOrganization/raw/gh-pages/img/7A.mp3"
        
        # radio images
        # x["normal"] = "https://cdn.gather.town/storage.googleapis.com/gather-town.appspot.com/internal-dashboard/images/GI1P36Mx4bsfd0QiRpsZQ"
        # x["highlighted"] = "https://cdn.gather.town/storage.googleapis.com/gather-town.appspot.com/internal-dashboard/images/94UIKDAQg3S8QEM3I9Fsz"
        print(x["sound"]["src"])
p = requests.post('https://gather.town/api/setMap', json={"apiKey": "doa91a6eaEZV6r5P", "spaceId": "bLC4E96xZ4dVKnTF\\testing", "mapId": "empty-room-small-brick", "mapContent": data })

if p.status_code != 200:
    print(str(p.status_code)+ ' '+p.reason)
else:
    print('success')
