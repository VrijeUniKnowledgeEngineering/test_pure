import requests
import json

data = {"data" : "24.3"}
data_json = json.dumps(data)

# Accept: application/json

headers = {'Accept': 'application/json'}

resp = requests.get('https://research.vu.nl/ws/api/59/persons?q=harmelen&apiKey=1aecc9b3-0b58-4e00-b757-c1a8026cbbfd',  headers=headers)
if resp.status_code != 200:
    # This means something went wrong.
    print('life is hard')
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))

print (resp)
print (resp.status_code)

response = resp.json()
print (response['items'][0]['name']['firstName'])

# for todo_item in resp.json():
#
#     print('{} {}'.format(todo_item['id'], todo_item['summary']))