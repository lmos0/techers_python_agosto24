import pandas as pd 


#DataFrame 

data = [
    ['Índia', 1490000000, 'Ásia'],
    ['China', 1444000000, 'Ásia' ],
    ['Estados Unidos', 331002651, 'América do Norte'],
    ['Indonésia', 273523615, 'Ásia' ],
    ['Paquistão', 220892331, 'Ásia'],
    ['Brasil', 203080756, 'América do Sul'],
    ['Nigéria', 206139587, 'África']
]



#Criar o DataFrame

df = pd.DataFrame(data, columns=['País', 'População', 'Continente'] )

print(df)

df.to_excel('populacao_v2.xlsx', index=False )