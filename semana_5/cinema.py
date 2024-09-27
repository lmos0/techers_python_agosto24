import requests

api_key = '35d90404' 
movie = input('Digite o nome do filme a ser consultado: ')

url = f'http://www.omdbapi.com/?t={movie}&apikey={api_key}&'

response = requests.get(url)

info_movie = response.json()

print('Título:', info_movie['Title'])
print('Ano de Lançamento:', info_movie['Year'])
print('Nota IMDB:', info_movie['imdbRating'])
print('Direção:', info_movie['Director'] )
print('Elenco:', info_movie['Actors'])
print('País de Origem:', info_movie['Country'])
