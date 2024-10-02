class Cachorro:
    def __init__(self, nome, raca, idade): # __ = dunder. __init__ método construtor, ele é responsável por criar uma instância de uma classe
        self.nome = nome 
        self.raca = raca
        self.idade = idade 

    
    def latir(self):
        print(f'{self.nome} diz: au-au')

cachorro1 = Cachorro('bob', 'vira-lata', 5) #Instância da classe cachorro
cachorro2 = Cachorro('Belinha', 'poodle', 28)

cachorro1.latir()
cachorro2.latir()


