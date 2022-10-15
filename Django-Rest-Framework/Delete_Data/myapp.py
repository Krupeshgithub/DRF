import json
import requests
url = 'http://127.0.0.1:8000/delete/'
data = {
    'id':3,
}
json_data = json.dumps(data)

r = requests.post(url=url,data=json_data)
# data = r.json()
# print(data)
