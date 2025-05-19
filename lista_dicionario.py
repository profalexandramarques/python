
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

# Acessando dados da lista
print(dados_pessoa[0]["nome"])  # Saída: João
print(dados_pessoa[1]["idade"]) # Saída: 25
pessoa = {
        "nome": "João",
        "idade": 30,
        "cidade": "São Paulo",
        "profissao": "Engenheiro",        
    }

pessoa["nome"] = input('Digite o nome: ')
pessoa["idade"] = int(input('Digite a idade: '))
pessoa["cidade"] = input('Digite a cidade: ')
pessoa["profissao"] = input('Digite a profissão: ')

dados_pessoa.append(pessoa)

# Escrevendo os dados da lista
for pessoa in dados_pessoa:
    print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Cidade: {pessoa['cidade']}")