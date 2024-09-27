import requests 

cep = input('Digite o CEP: ')

url = f'https://viacep.com.br/ws/{cep}/json/'

response = requests.get(url)

#print(response.json()) #Corresponde a buscar o arquivo JSON inteiro/dicionário Python inteiro
print('Endereço:', response.json()['logradouro'])
print('Cidade:', response.json()['localidade'])
print('Unidade Federativa:', response.json()['estado'], response.json()['uf'])
print('CEP:', response.json()['cep'])


