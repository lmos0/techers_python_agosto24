nota = int(input('Digite a nota recebida pelo aluno: '))

if nota >= 90:
    print("A")

elif nota >= 80:
    print('B')

elif nota >= 70:
    print('C')

elif nota >= 60:
    print('D')

else:
    print('F')

#If testa uma condição
#Elif ele esta a condição ATÉ encontrar a primeira condição verdadeira
#Else é executado caso nenhuma das condições anteriores sejam verdadeiras