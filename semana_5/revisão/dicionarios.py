#Criar um dicionário pra cadastrar alunos

def cadastrar_alunos():
    alunos = {} #Dentro do escopo da função. E precisa ser retornado para ser acessado pelo restante código

    while True:
        nome = input('Digite o nome do aluno (ou deixe vazio para encerrar o programa) ')
        if nome == '':
            break
        idade = int(input(f'Digite a idade do {nome}: '))
        alunos[nome] = idade
    return alunos
    


alunos_cadastrados = cadastrar_alunos()

print(alunos_cadastrados)