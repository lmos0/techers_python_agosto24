import pandas as pd

df = pd.read_csv('idh_mundial.csv')
df2 = pd.read_excel('populacao_v2.xlsx')

df_united = pd.concat([df, df2]).to_excel('tabelas_unidas.xlsx', index=False)

print(df_united)