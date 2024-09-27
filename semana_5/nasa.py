import requests

api_key = 'ov5Ocfk0sanwsHNTyZpJOueLSFu9YLELO6iUZEQW'

lon = input('Digite a Longitude: ')

lat = input('Digite a Latitude: ')

data = input("Digite a data desejada, aaaa-mm-dd ")

url = f'https://api.nasa.gov/planetary/earth/imagery?lon={lon}&lat={lat}&date={data}&dim=0.15&api_key={api_key}'

response = requests.get(url)

print(response.status_code)
url_imagem = response.json().get('url')
print(url_imagem)
