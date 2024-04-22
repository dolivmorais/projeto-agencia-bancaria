from datetime import datetime
import pytz


class ContaCorrente:
    
    @staticmethod
    def data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')
        
    
    def __init__(self, nome, cpf, agencia, num_conta) -> None:
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []

    def consultar_saldo(self):
        print("Seu saldo atual e de: R${:,.2f}".format(self.saldo))

    def depositar(self, valor):
        self.saldo =+ valor
        self.transacoes.append((valor,self.saldo,ContaCorrente.data_hora()))

    def limite_conta(self):
        self.limite = -1000
        return self.limite
        
    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self.limite_conta():
            print("Você não tem saldo suficiente para sacar esse valor!")
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((-valor,self.saldo,ContaCorrente.data_hora()))

    def consultar_limite_da_conta(self):
        print('Seu limite é de R${:,.2f}'.format(self.limite_conta()))

    def consultar_historico_transacoes(self):
        print('Historio de Transaçoes')
        print('valor, saldo, data_hora')
        for transacoes in self.transacoes:
            print(transacoes)


    

# programa

conta1 = ContaCorrente('aaa','1351648648',54,5748486)
conta1.consultar_saldo()
conta1.depositar(10000)
conta1.consultar_saldo()
conta1.sacar_dinheiro(10500)
conta1.consultar_saldo()

conta1.consultar_limite_da_conta()
print("*-" * 20) 

conta1.consultar_historico_transacoes()




