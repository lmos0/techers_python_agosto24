class ClientePadrao:
    def __init__(self, nome:str, cpf:str, conta_corrente:str, saldo:float = 0, cheque_especial:float = 0, pre_credito:float = 0, ativo:bool = True ):
        #saldo = 0. Por padrão o objeto vai ser iniciado com valor de 0. Salvo informado um valor distinto ao ser criado
        self.nome = nome
        self.cpf = cpf
        self.conta_corrente = conta_corrente
        self.ativo = ativo
        self.saldo = saldo
        self.cheque_especial = cheque_especial
        self.pre_credito = pre_credito
        #Definição dos atributores que serão recebidos no momento da criação do objeto. Ou seja, quando for utilizado ClientePadrao('luis', 213.222)'
   
    def informar(self):
        print(f'Nome: {self.nome} - CPF: {self.cpf} - CC: {self.conta_corrente} - Cliente Ativo: {self.ativo} - Saldo: {self.saldo}, - Cheque Especial: {self.cheque_especial} - Crédito pré-aprovado: {self.pre_credito}')
    
    
    def depositar(self, valor_do_deposito:float):
        if self.ativo == False:
            print('Solicitação negada. Conta desativada')
            return
        self.saldo = self.saldo + valor_do_deposito #self.saldo += valor_do_deposito
        print(f'Depósito de {valor_do_deposito} realizado com sucesso. Saldo atual: R$ {self.saldo}')
    
    def sacar(self, valor_sacado:float):
        if self.ativo == False:
            print('Solicitação negada. Conta desativada')
            return
        if self.saldo + self.cheque_especial >= valor_sacado:
            self.saldo = self.saldo - valor_sacado
            print(f'Saque de R$ {valor_sacado} realizado com sucesso. Saldo atual: R$ {self.saldo}')
        else:
            print('Saldo insuficiente')
    
    def consultar_saldo(self):
        print(f'Saldo atual: R${self.saldo}')

    def desativar_conta(self):
        self.ativo = False
        print(f'{self.ativo}. Conta desativada com sucesso')

    def ativar_conta(self):
        self.ativo = True
        print(f'{self.ativo}. Conta ativada com sucesso')





