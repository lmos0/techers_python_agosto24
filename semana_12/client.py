import hashlib

senha = '2' #senha que o usuário enviou. E que precisa ser hasheada antes de salvo no banco de dados

senha_hasheada = hashlib.sha256(senha.encode()).hexdigest() #salvar no banco de dados
print(senha_hasheada)

