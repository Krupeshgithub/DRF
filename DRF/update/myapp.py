import requests
import json

url = "http://127.0.0.1:8000/str"
def update_data():
    data = {
        'id':2,
        'name':'Ramju',
        'city' : 'hjdasfd',
    }
    json_data = json.dumps(data)
    r = requests.put(url = url,data = json_data)
update_data()    