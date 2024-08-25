import requests

output = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

results = output.json()


for i in range(len(results)):
  print(results[i]["user"]["login"])