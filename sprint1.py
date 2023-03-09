from urllib import request
import json
import requests
import secrets

base_url: str = 'https://ssahu.wufoo.com/api/v3/'
password_manager = request.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, base_url, secrets.username, secrets.password)
handler = request.HTTPBasicAuthHandler(password_manager)
opener = request.build_opener(handler)

request.install_opener(opener)

response = request.urlopen(base_url + "forms.json")
data = json.load(response)

# print(json.dumps(data, indent=4, sort_keys=True))
print(data["Forms"][0]["LinkEntries"])

response = requests.get(data["Forms"][0]["LinkEntries"], auth=(secrets.username, secrets.password))

print(response.status_code)

entries = response.json()
with open("swap.json", "w") as outfile:
    json.dump(entries, outfile)
print(entries)


def response() -> object:
    return response().status_code
