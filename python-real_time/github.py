import requests

output =   requests.get("https://api.github.com/repos/thiru1512/python-scripts/branches")


details = output.json()

print(details)

details[0]["name"]="new"

for info in details:
    print(info["commit"]["url"])
    print(info["name"])