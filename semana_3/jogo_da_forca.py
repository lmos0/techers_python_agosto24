import random


# Sortear e escolher uma palavra para ser utilizada


def escolher_palavra():

    lista_de_palavras =[ "python",
    "programacao",
    "desenvolvimento",
    "algoritmo",
    "computador",
    "tecnologia",
    "software",
    "hardware",
    "internet",
    "dados"
    ]

    return random.choice(lista_de_palavras) 


# Exibir a quantidade de letras dessa palavra, sem mostrar qual é a palavra _ _ _ _ _ _

def exibir_palavra(palavra):
   pass


def jogo_em_execucao():
    palavra_da_rodada = escolher_palavra()
    letras_corretas = []
    letras_erradas = []
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")

    while tentativas > 0:
        letra_chutada = input('Digite uma letra: ').lower()
        print(f'Você já usou as seguintes letras {letras_corretas+ letras_erradas} ')

        if letra_chutada in palavra_da_rodada:
            letras_corretas.append(letra_chutada)
            print(f'Sucesso! A letra {letra_chutada} está na palavra')
        
        else:
            letras_erradas.append(letra_chutada)
            tentativas -= 1 # tentativas = tentativas -1
            print(f'A letra {letra_chutada} não está na palavra')




# Perguntar para o jogador qual letra ele vai chutar
# Conferir se há a letra na palavra. Se houver, mostre a letra escolhida. Senão retire tentativas do jogador

