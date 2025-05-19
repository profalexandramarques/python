#Algoritmo que leio o nome e o ano atual
print('=== Ano Atual ===')
#Leitura da tela
nome = input('Digite o seu nome: ')
ano_atual = int(input('Digite o ano atual'))
ano_nasc = int(input('Digite o ano de nascimento'))
#Calculo da idade
idade = ano_atual - ano_nasc
#Escrita na tela
print('Nome',nome)
print('Ano ',ano_atual)
print('Idade ',idade)