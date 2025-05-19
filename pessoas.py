
dados_pessoa = [ 
    {
        "nome": "João",
        "idade": 30,
        "cidade": "São Paulo",
        "profissao": "Engenheiro",        
    },
    {
        "nome": "Maria",
        "idade": 25,
        "cidade": "Rio de Janeiro",
        "profissao": "Designer",
    },
    {
        "nome": "Pedro",
        "idade": 35,
        "cidade": "Belo Horizonte",
        "profissao": "Professor",
    },
    {
        "nome": "Ana",
        "idade": 18,
        "cidade": "Caxias do Sul",
        "profissao": "Desenvolvedora",
    }
]

def cadastro(dados_pessoa):
    #Informar os dados no dicionario
    pessoa = {
        "nome": "",
        "idade": 0,
        "cidade": "",
        "profissao": ""        
    }
    pessoa["nome"] = input('Digite o nome: ')
    pessoa["idade"] = int(input('Digite a idade: '))
    pessoa["cidade"] = input('Digite a cidade: ')
    pessoa["profissao"] = input('Digite a profissão: ')
    #Adiciona a pessoa na lista
    dados_pessoa.append(pessoa)

# Escrevendo os dados da lista
def listar_pessoas(dados_pessoa): 
    i = 1   
    for pessoa in dados_pessoa:
        print(f"{i} - Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Cidade: {pessoa['cidade']}, Profissão: {pessoa['profissao']}")
        i += 1

#Calcular a média de idade
def calcular_media_idade(dados_pessoa):
    media = 0
    soma = 0
    i = 0
    for pessoa in dados_pessoa:        
        soma = soma + pessoa['idade'];
        i+=1
        
    if (soma > 0):
        media = soma/i
    return media      

# Acessando dados da lista
#print(dados_pessoa[0]["nome"])  # Saída: João
#print(dados_pessoa[1]["idade"]) # Saída: 25


#Principal
print('=== Cadastro de Pessoas ESP === ')
opcao = ''
while(opcao != '9'):
    print('Operações: 1 - Cadastro, 2 - Listar Pessoas, 3 - Calcular a média de idade, 9 - Sair')
    opcao = input('Digite a opção: ')
    #Leia da tela
    if(opcao == '1'):
        cadastro(dados_pessoa)
    elif (opcao == '2'):
        listar_pessoas(dados_pessoa)
    elif (opcao == '3'):
        print(calcular_media_idade(dados_pessoa))    
    elif (opcao == '9'):
        print('Volte sempre!') 


