from datetime import datetime
import pytz
from random import randint


class ContaCorrente:
    """
    Cria um objeto de ConntaCorrente oara gerenciar as contas dos clientes.
    Atributos:
        nome: nome do cliente
        cpf: do cliente
        agencia: responsavel pela conta
        num_conta: numero da conta do clinte
        limite: da conta
    """
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
        self.cartoes = []

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

    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor,self.saldo,ContaCorrente.data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor,conta_destino.saldo,ContaCorrente.data_hora()))


class CartaoCredito:

    @staticmethod
    def data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self,titular,conta_corrente) -> None:
        self.numero = randint(100000000000000,9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito.data_hora().month,CartaoCredito.data_hora().year +4)
        self.cod_seguranca = '{}{}{}'.format(randint(0,9),randint(0,9),randint(0,9))
        self.limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print("Nova senha invalida!")

