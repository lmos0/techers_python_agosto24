from ContaPadrao import ClientePadrao
from ClienteGold import ClienteGold
from ClienteSilver import ClienteSilver


#Conceito de aproveitar métodos e atributos de outra classe é chamado de Herança

conta0 = ClientePadrao('Luís', '232.323.543-21', '3311')
conta1 = ClienteSilver('Arthur', '123.456.789-00', '1221')
conta2 = ClienteGold('Mariana', '987.654.321-11', '9943')

# conta0.deposito(300.00)
# conta0.saque(150.50)

conta0.informar()
conta1.informar()
conta2.informar()

conta2.desativar_conta()

conta2.depositar(1000)
conta2.informar()
