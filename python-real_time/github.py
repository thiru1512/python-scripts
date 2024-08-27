import requests

output =   requests.get("https://api.github.com/repos/thiru1512/python-scripts/branches")



response = output.json()
print(response)

response[0]["name"]="new"

for info in response:
    print(info["commit"]["url"])
    print(info["name"])