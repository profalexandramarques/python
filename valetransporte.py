#Calculo do Vale transporte 6%
#6 % = 0.06 ou 6/100
#Constante
percentual = 0.06
#Leitura da tela
nome = input('Digite o nome do colaborador: ')
salario = float(input('Digite o salário bruto: '))
#Calculo do desconto
vale_transp = salario * percentual
salario_liq = salario - vale_transp
#Mostra na tela
print('==== Dados da Folha ====')
print('Nome:', nome)
print('Vale Transporte:', round(vale_transp,2))
print('Salário Líquido:', round(salario_liq,2))