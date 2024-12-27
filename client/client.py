import requests

# ip = '127.0.0.1'
ip = 'localhost'
port = 30502
endpoint = 'api/recommend'

url = f'http://{ip}:{port}/{endpoint}'
data = {"songs": ['Mask Off', 'DNA.']}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=data, headers=headers)
print(f'[Status Code]: {response.status_code}\n[Text]: {response.text}')

with open('response.out', 'w') as f:
    f.write(f'Status Code: {response.status_code}\n')
    f.write(f'Response Headers: {response.headers}\n')
    f.write(f'Response Body: {response.text}\n')