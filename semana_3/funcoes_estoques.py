estoque = {}

def adicionar_estoque(item, quantidade):
    estoque[item] = estoque.get(item,0) + quantidade

def atualizar_estoque(item, nova_quantidade):
    estoque[item] = nova_quantidade

def verificar_estoque(item):
    if item in estoque:
        return f'O {item} está disponível em estoque'
    else:
        return 'Não há nenhuma unidade do item no estoque'

def remover_item_estoque(item, quantidade_a_ser_removida):
    if item in estoque:
        estoque[item] -= quantidade_a_ser_removida
        if estoque[item] <= 0:
            del estoque[item]

def mostrar_estoque():
    print(estoque)