import pandas as pd

df = pd.read_csv('idh_mundial.csv')
df2 = pd.read_excel('maiores_45.xlsx')

print(df.tail(2)) #Acessa informações a partir do final da tabela. Argumento (x) determina a quantidade de linhas a serem acessadas

print(df2.head(2)) #Acessa informações a partir do início da tabela. Argumento (x) determina a quantidade de linhas a serem acessadas

print(df.loc[2]) #Informações referentes a uma linha específica 