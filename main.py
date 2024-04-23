from contas_bancos import ContaCorrente, CartaoCredito

conta1 = ContaCorrente('aaa','1351648648',54,5748486)
cartao1 = CartaoCredito('aaa',conta1)

nova_senha = cartao1.senha = '1222'
print(nova_senha)