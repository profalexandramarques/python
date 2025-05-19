#Media
#Ler duas notas da tela
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
#Calcular a média
media = (n1+n2) / 2
print(media)
#Comando condicional - Exame
if (media > 6):
    print('Aprovado! Média = ',round(media,1))
elif (media == 6):
    print('Exame! Média = ',round(media,1))
else:
    print('Reprovado! Média = ',round(media,1))