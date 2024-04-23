class Agencia:

    def __init__(self,telefone,cnpj,num_agencia) -> None:
        self.telefone = telefone
        self.cnpj = cnpj
        self.num_agencia = num_agencia
        self.clientes = []
        self.caixa = 2000
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo no nivel recomendado. Caixa atual R${:,.2f}'.format(self.caixa))
        else:
            print('Caixa esta ok. Saldo atual R${:,.2f}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cnpj, juro):
        if self.caixa > valor:
            self.emprestimos.append((valor,cnpj,juro))            
        else:
            print('Saldo em caixa é insuficiente para este valor!')

    def adiconar_clientes(self,nome, cpf, patrimonio):
        self.clientes.append((self,nome, cpf, patrimonio))

#agencia virtual
class AgenciaVirtual(Agencia):

    pass

#agencia comum
class AgenciaComum(Agencia):
    
    pass

#agencia premium
class AgenciaPremium(Agencia):
    pass
