import pandas as pd

df = pd.read_excel(r"C:\Users\luis.santos\Downloads\aula.xlsx")
#raw 

#print(df[df['Idades'] > 30]) #Devolve os elementos com idade maior que 30

specific_name = df[df['Nomes'] == 'Laura Martins']
#print(specific_name)

print(df)
#Procurar nomes

searching_names = ['João Pereira', 'Gabriel Rodrigues']

#print('Busca usando isin', df[df['Nomes'].isin(searching_names)])

search_fragments = df[df['Nomes'].str.contains('Ga')]

searching_numbers_default = df[df['Idades'] > 25]

searching_numbers_chaos = df[pd.to_numeric(df['Idades'], errors='coerce').notna()]

print(df[df['Idades']  > 30].sort_values(by='Idades', ascending=False))

df[df['Idades']  > 45].to_excel('maiores_45.xlsx', index=False)