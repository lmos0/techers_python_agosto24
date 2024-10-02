class Livro:
    def __init__(self, titulo:str, autor:str, editora:str, numero_de_paginas:int, status_de_disponibilidade=True): #método construtor. Função Criar uma instância de um novo objeto, usando informações definidas na classe
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.numero_de_paginas = numero_de_paginas
        self.status_de_disponibilidade = status_de_disponibilidade
    
    # def __str__(self):
    #      return f'{self.titulo}, {self.autor}, {self.editora}, {self.numero_de_paginas}'

    def extrair_informacoes(self):
        print(f'**Título** \t {self.titulo}')
        print(f'**Autor** \t {self.autor}')
        print(f'**Editora** \t {self.editora}')
        print(f'**Número de Páginas** \t {self.numero_de_paginas}')

    def emprestar_livro(self):
        self.status_de_disponibilidade = False
    
    def devolver_livro(self):
        self.status_de_disponibilidade = True
        


livro1 = Livro("A Revolução dos Bichos", 'George Orwell', 'Cia das Letras', 128) #A ORDEM IMPORTA
livro2 = Livro('O Senhor dos Anéis: A Sociedade do Anel', 'J.R.R. Tolkien', 'Martins Fontes', 504  )

print(livro1.status_de_disponibilidade)

livro1.emprestar_livro()

print(livro1.status_de_disponibilidade)

