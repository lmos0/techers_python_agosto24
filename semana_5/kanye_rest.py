import requests

url = 'https://api.kanye.rest'

response = requests.get(url)

print(response.json())