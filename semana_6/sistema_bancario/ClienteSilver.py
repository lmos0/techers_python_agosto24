from ContaPadrao import ClientePadrao

class ClienteSilver(ClientePadrao):
    def __init__(self, nome:str, cpf:str, conta_corrente:str, saldo:float = 0):
       super().__init__(nome, cpf, conta_corrente, saldo, cheque_especial=1000, pre_credito=0) 