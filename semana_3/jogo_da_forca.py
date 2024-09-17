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

def exibir_palavra(palavra, letras_corretas):
    exibicao = ""

    for letra in palavra:
        if letra in letras_corretas:
            exibicao += letra + " "
        else:
            exibicao += "_ "
    print('Palavra:', exibicao.strip())
    

def verificar_vitoria(palavra_da_rodada, letras_corretas):
    for letra in palavra_da_rodada:
        if letra not in letras_corretas:
            return False
    return True

#Função com retorno booleano. Verdadeiro ou Falso. => Se o jogo terminou ou não


def jogo_em_execucao():
    palavra_da_rodada = escolher_palavra()
    letras_corretas = []
    letras_erradas = []
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")

    while tentativas > 0:

        exibir_palavra(palavra_da_rodada, letras_corretas)
        print(f'Você tem {tentativas} tentativas')
        letra_chutada = input('Digite uma letra: ').lower()

        #Certificar que o usuário não usuará uma letra repetida. 
        if letra_chutada in letras_corretas or letra_chutada in letras_erradas:
            print(f'Você já usou a letra {letra_chutada}. Tente outra vez')
            continue

        if letra_chutada in palavra_da_rodada:
            letras_corretas.append(letra_chutada)
            print(f'Sucesso! A letra {letra_chutada} está na palavra')
        
        else:
            letras_erradas.append(letra_chutada)
            tentativas -= 1 # tentativas = tentativas -1
            print(f'A letra {letra_chutada} não está na palavra')


        if verificar_vitoria(palavra_da_rodada, letras_corretas):
            exibir_palavra(palavra_da_rodada,letras_corretas)
            print('Parabéns, você acertou a palavra!')
            break

    else:
        print(f'Você perdeu! A palavra era: {palavra_da_rodada}')


jogo_em_execucao()
# Perguntar para o jogador qual letra ele vai chutar
# Conferir se há a letra na palavra. Se houver, mostre a letra escolhida. Senão retire tentativas do jogador

