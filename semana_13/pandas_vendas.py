import pandas as pd 
import os #biblioteca utilizada para manipular o sistema operacional

def get_city(address):
    return address.split(',')[1]



all_data = pd.read_csv('all_data.csv')

all_data['Month'] = all_data['Order Date'].str[0:2]

nan_df = all_data[all_data.isna().any(axis=1)]

all_data = all_data.dropna(how='all')

all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']
all_data['Month'] = all_data['Month'].astype('int32') #Conversão não pode haver NaNs e nem palavras


all_data['Sales'] = all_data['Quantity Ordered'].astype('int32') * all_data['Price Each'].astype('float') #Criando a tabela Sales e convertendo os dados necessários


##Descobrir qual mês teve maior valor  de vendas##

#results = all_data.groupby('Month').sum(['Sales'])
#formatted_results = results.applymap(lambda x: f"{x:.2f}")


all_data['City'] = all_data['Purchase Address'].apply(lambda x: get_city(x))

city_results = all_data.groupby('City').sum(['Sales'])
print(city_results)

all_data.to_csv('all_data_modified.csv', index=False)


######### Juntando as tabelas da pasta Salves_Data ######

# files = [file for file in os.listdir(r"C:\Users\luis.santos\Downloads\Sales_Data") ] #listando todos os arquivos na pasta

# all_months_df = pd.DataFrame()

# for file in files:
#     df = pd.read_csv(r"C:\Users\luis.santos\Downloads\Sales_Data" + "\\" + file)
#     #df = pd.read_csv(os.path.join("C:\Users\luis.santos\Downloads\Sales_Data", file))
#     all_months_df = pd.concat([all_months_df, df])

# all_months_df.to_csv('all_data.csv' , index=False)

######### Juntando as tabelas da pasta Salves_Data ######

