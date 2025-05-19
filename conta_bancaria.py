import time
#Conta Bancária
#Saque
def saque(valor,saldo,movimentacoes):
    if(valor<=saldo):
       saldo = saldo - valor
       print('Saque efetuado com sucesso!')
       movimentacoes.append('Saque R$ '+str(valor))
    else:
        print('Saldo insuficiente!')   

    return saldo    
#Depositar
def deposito(valor,saldo,movimentacoes):
    saldo = saldo + valor
    print('Depósito efetuado com sucesso!')
    movimentacoes.append('Depósito R$ '+str(valor))
    return saldo
    
#Ver saldo
def ver_saldo(saldo):
    print('=== Saldo ===')
    print('O seu saldo é R$',saldo)

#Extrato
def extrato(movimentacoes):
    print('=== Extrato ===')
    for descricao in movimentacoes:
        print(descricao)
    print('================')
    time.sleep(5)

#Pagar Boleto
def pagar_boleto(valor, saldo, movimentacoes):
    if(valor<=saldo):
       saldo = saldo - valor
       print('Boleto Pago com sucesso!')
       movimentacoes.append('Boleto R$ '+str(valor))
    else:
        print('Não foi possivel pagar o boleto: saldo insuficiente!')   

    return saldo    

#Principal
saldo = 1000
movimentacoes = ['Saldo inicial = R$ 1000']
print('=== Bank ESP === ')
opcao = ''
while(opcao != '9'):
    print('Operações: 1 - Saldo, 2 - Saque, 3 - Deposito, 4 - Pagar Boleto, 5 - Extrato')
    print('9 - Sair')
    opcao = input('Digite a operação bancária: ')
    #Leia da tela
    if(opcao =='1'):
       ver_saldo(saldo)
    elif (opcao == '2'):
       valor = float(input("Digite o valor a sacar: "))
       if (valor > 0):
          saldo = saque(valor,saldo,movimentacoes)
          ver_saldo(saldo)
       else:
           print('Valor inválido!')
    elif (opcao == '3'):
        valor = float(input("Digite o valor a depositar: "))
        if (valor > 0):
          saldo = deposito(valor,saldo,movimentacoes)
          ver_saldo(saldo)
        else:
           print('Valor inválido!')
    elif (opcao == '4'):
       valor = float(input("Digite o valor do boleto: "))
       if (valor > 0):
          saldo = pagar_boleto(valor,saldo,movimentacoes)
          ver_saldo(saldo)
       else:
           print('Valor inválido!')       
    elif(opcao == '5'): 
        extrato(movimentacoes) 
    elif(opcao == '9'): 
        print('Encerrando atendimento...')
        time.sleep(5)
    else:
        print('Operação inválida')       