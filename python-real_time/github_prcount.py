import requests

url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"

response = requests.get(url)



if response.status_code == 200:
    pull_requests = response.json()

    pr_creators = {}

    for pull in pull_requests:
        username = pull ["user"]["login"]
        
        if username in pr_creators:
            pr_creators[username] += 1
        else:
            pr_creators[username] = 1
    
    print("PR Creators and Counts:")
    

    for username,count in pr_creators.items():
        print(f"{username}: {count}PR(s)")

else:
    print(f"unable to reach{response.status_code}")    

