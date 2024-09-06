#Estrutura dicionário

listinha = ['açucar', 'sal', 35, {}]
dicionario = {}

lista_de_cadastro_com_emails = {
    "Luis":34,
    "Mariana": 'mariana@gmail.com', 
    'Arthur':'arthur@hotmail.com'
}

# print(lista_de_cadastro_com_emails['Luis'])
# print(lista_de_cadastro_com_emails.get('Mariana'))

# print(len(lista_de_cadastro_com_emails))

traducoes_da_palavra_picante = {
    "Inglês": 'spicy',
    'Espanhol': 'picante',
    'Francês': 'épicé',
    'Italiano': 'piccante',
    'Japonês': '辛い' #karai
}

palavra = input('Digite o idioma o qual você deseja a tradução: ').capitalize()
if palavra.capitalize() in traducoes_da_palavra_picante:
    print(f'A tradução é {traducoes_da_palavra_picante[palavra]}')

else:
    print('Tradução não encontrada')