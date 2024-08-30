import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://thiru1512.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth("thiruthiru19@gmail.com", "ATATT3xFfGF0_UgXDy9l9fhkmsMwU1x7urvhf2FrpR0RZA7ps1Pazfl2EUHHu3S-6RH2S9L188jtNQRzC3_7-1nifQs8UBHpoB2uC1DFQa5onLFrcKEQ0x-WLJW_jS_XTQM5LlWhITH8MKUrj1dqBPvXawSVk8nzHGo4wgjZRVMIFDEoWL4ubVk=04A54F0A")

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "This is my first jirs issue creation",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10008"
    },
    "project": {
      "key": "DEV"
    },
   
    "summary": "First Jira ticket",
},
  "update": {}

} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

