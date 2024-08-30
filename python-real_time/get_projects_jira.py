# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os

baseurl = "thiru1512.atlassian.net"
url = f"http://{baseurl}/rest/api/2/project"

auth = HTTPBasicAuth(os.getenv("email_id"),os.getenv("api_token"))

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

for name in output:
    print(name["name"])




