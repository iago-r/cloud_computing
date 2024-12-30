import requests, time

count = 0

ip = 'localhost'
port = 32030
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

# Abrir 'response.out' uma vez, para sobrescrever a cada requisição
with open('response.out', 'w') as f:
    while True:
        response = requests.post(url, json=data, headers=headers)
        
        print(f'[{count + 1}] [Status Code]: {response.status_code}')
        print(f'[Response Body]: {response.text}\n')

        f.write(f'Attempt {count + 1}:\n')
        f.write(f'Status Code: {response.status_code}\n')
        f.write(f'Response Headers: {response.headers}\n')
        f.write(f'Response Body: {response.text}\n')
        f.write('-' * 80 + '\n')

        time.sleep(1)
        count += 1

print("Número máximo de requisições atingido. Loop interrompido.")