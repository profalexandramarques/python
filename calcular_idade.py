import datetime
hoje = datetime.datetime.now()
#Escreve a data e hora de hoje 
ano = hoje.year
print('Ano atual',ano)

data_nascimento = input('Digite a data de nascimento: ')
dtnasc = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
print(dtnasc)

aniversario = datetime.datetime(ano,dtnasc.month,dtnasc.day)
if aniversario < hoje:
    aniversario = datetime.datetime(ano+1,dtnasc.month,dtnasc.day)
print(aniversario)

idade = hoje - dtnasc
print("Sua idade é ",round(idade.days/365),'anos')

diferenca = aniversario - hoje
print("Faltam",diferenca.days+1,"dia(s )para seu aniversario")

