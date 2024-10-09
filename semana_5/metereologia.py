import requests 

"""
- Temperatura atual (`temp`)
- Umidade (`humidity`)
- Descrição do tempo (`description`)
- Nome da Cidade (`name`)
- País (`country`)

O link a ser consultado “https://api.openweathermap.org/data/2.5/weather?q=cidade_a_ser_consultado&appid=chave_da_api&units=metric”

"""

#Desenvolver um script em Python que consuma a API do OpenWeatherMap para obter dados meteorológicos de uma cidade específica.

chave_api = '5738ebfb04d69d4df99d102275978e92' #Chave API é uma string

cidade_a_ser_consultada = input('Digite a cidade que você deseja buscar informações: ')

url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade_a_ser_consultada}&appid={chave_api}&units=metric'

resposta = requests.get(url)
data = resposta.json() #Json formato muito semelhante ao dict do Python

main = data['main']

temperatura = main['temp']
umidade = main['humidity']
main_descricao = data['weather'][0]

descricao = main_descricao['description']

sys = data['sys']
pais = sys['country']
cidade = data['name']

print(f'Cidade: {cidade}')
print(f'País: {pais}')

print(f'Temperatura de {temperatura}, umidade relativa do ar {umidade}% e o tempo está {descricao}')