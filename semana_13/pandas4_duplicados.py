import pandas as pd 

df = pd.read_excel('aula_pandas_duplicado.xlsx')
print(df)

print(df.drop_duplicates(['Nomes']))

df.drop_duplicates(['Nomes']).to_excel('aula_pandas_sem_duplicados.xlsx', index=False)