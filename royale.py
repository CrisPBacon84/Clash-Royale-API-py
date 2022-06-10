import urllib.request
import json

user_tag = input("Enter palyer tag to get data: ")

with open("key.txt") as f:
    my_key = f.read().rstrip("/n")
    base_url = "https://api.clashroyale.com/v1"
    endpoint = "/players/%23" + user_tag
    request = urllib.request.Request(
                    base_url+endpoint,
                    None,
                    {
                        "Accept": "application/json",
                        "Authorization": "Bearer %s" % my_key
                    } 
                )
    response = urllib.request.urlopen(request).read().decode("utf-8")
    data = json.loads(response)
    print(response)