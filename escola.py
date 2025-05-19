#Bibliotecas
import sqlite3
import time

#Criação da base de dados
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

#Criação da tabela pessoas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        fone TEXT,
        tipo int 
    )
''')

#Criação da tabela boletim
cursor.execute('''
    CREATE TABLE IF NOT EXISTS boletim (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno INTEGER,
        nota1 REAL,
        nota2 REAL,
        frequencia INTEGER,
        media REAL,
        conceito TEXT               
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cursos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        valor REAL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS turmas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        curso INTEGER,
        professor INTEGER, 
        ano INTEGER,
        FOREIGN KEY(professor) REFERENCES pessoas(id)               
    )
''')

conn.commit()

#Função para ler o último código
def ler_ultimo():
    cursor.execute("SELECT max(id) FROM pessoas")
    resultado = cursor.fetchone()
    return resultado[0]

# Função para criar uma nova pessoa
def criar_pessoa(nome, email,fone, tipo):
    cursor.execute('''INSERT INTO pessoas (nome, email,fone, tipo) 
                   VALUES (?, ?, ?, ?)''', (nome, email,fone, tipo))
    conn.commit()
    return ler_ultimo()

#Função para ler todas as pessoas
def ler_pessoas():
    cursor.execute("SELECT * FROM pessoas ")
    return cursor.fetchall()  

#Função para mostrar todos os alunos por ordem alfabética de nome
def mostrar_alunos():
    cursor.execute('''SELECT * FROM pessoas 
                   WHERE tipo = 1 
                   ORDER BY nome ''')
    return cursor.fetchall()  

#Função para mostrar todos os professores por ordem alfabética de nome
def mostrar_professores():
    cursor.execute('''SELECT id, nome FROM pessoas 
                   WHERE tipo = 3 
                   ORDER BY nome ''')
    return cursor.fetchall() 

def listar_professores():
    dados_pessoa = mostrar_professores()
    for pessoa in dados_pessoa:
      print(pessoa)

#Ler uma pessoa pelo id
def ler_pessoa(id):    
    cursor.execute("SELECT * FROM pessoas WHERE id = ?",(id))
    resultado = cursor.fetchone()
    print(resultado[1])  
    return resultado
    

# Função para atualizar uma pessoa
def atualizar_pessoa(id, nome, email, fone):
    cursor.execute('''UPDATE pessoas SET nome = ?, email = ?, fone = ? 
                   WHERE id = ?''', (nome, email, fone, id))
    conn.commit() 

#Função para atualizar o e-mail da pessoa pelo ID
def atualizar_email(id, email):
    cursor.execute('''UPDATE pessoas SET email = ? 
                   WHERE id = ?''', (email, id))
    conn.commit() 

# Função para excluir uma pessoa
def excluir_pessoa(id):
    cursor.execute("DELETE FROM pessoas WHERE id = ?", (id))
    conn.commit()

#Inserir boletim
def inserir_boletim(aluno, nota1, nota2, frequencia, media, conceito):
    cursor.execute(''' INSERT INTO boletim (aluno, nota1, nota2, frequencia, media, conceito) 
                   VALUES (?, ?, ?, ?, ?, ?)''', 
                   (aluno, nota1, nota2, frequencia, media,conceito))
    conn.commit()

#Função para ler os dados do boletim
def ler_boletim():
    cursor.execute("SELECT * FROM boletim ")
    return cursor.fetchall()  

#Função mostrar o boletim de um aluno com seu nome
def mostrar_boletim(id):
    cursor.execute('''SELECT a.nome, b.media, b.conceito 
                   FROM boletim b 
                   INNER JOIN pessoas a
                   ON a.id = b.aluno
                   WHERE a.id = ?
                   ''',(id))
    return cursor.fetchall()  

#Inserir a turma no banco de dados
def inserir_turma(nome, professor, curso, ano):
    cursor.execute(''' INSERT INTO turmas (nome, curso, professor, ano) 
                   VALUES (?, ?, ?, ?)''', 
                   (nome, curso, professor, ano))
    conn.commit()

#Ler os dados da turma pelo nome da turma
def ler_turma(nome):    
    sql = "SELECT * FROM turmas WHERE nome = "+nome
    cursor.execute(sql)
    return cursor.fetchall()  

#Criar turma
def criar_turma():
    nome = input('Digite o nome da turma: ')
    listar_professores()
    professor = int(input('Digite o id do professor da turma: '))
    curso = input('Digite o curso: ')
    ano = int(input('Digite ano da turma: '))
    inserir_turma(nome, professor, curso, ano)
    print('Turma inserida com sucesso!')

#Principal
print("=== Escola ESP ===")
opcao = 0
while (opcao != '9'):
    print('\nSou Assistente Virtual ESP. Em que posso ajudar hoje?')
    print(''' 1 - Cadastro da Pessoa \n 2 - Ver dados da Pessoa \n 3 - Alterar \n 4 - Excluir \n 5 - Boletim 
6 - Mostrar os alunos \n 7 - Mostrar todas as pessoas 
8 - Mostrar Boletim \n 10 - Cadastrar Turma \n 11 - Pesquisar turma pelo nome \n 9 - Encerrar''')
    opcao = input('Por favor, digite apenas o número da operação desejada: ')
    if opcao == '1':
        print("=== Cadastro do Pessoa ===")
        tipo = int(input('Digite 1 - Aluno ou 2 - Responsável ou 3 - Professor: '))
        if (tipo == 1 or tipo == 2 or tipo == 3):
             nome = input('Digite o nome: ')
             email = input('Digite o email: ')
             fone = input('Digite o fone: ')
             id = criar_pessoa(nome,email, fone, tipo)
             print('O código da pessoa é ',id)            
        else:
            print('Tipo inválido!')
        time.sleep(2)  
    elif opcao == '2':
        print("Ver dados de uma pessoa")
        id = input('Digite o código da pessoa: ')
        dados_pessoa = ler_pessoa(id)
        if len(dados_pessoa) != 0:
           print(dados_pessoa)
        else:
           print("Pessoa não encontrada!")
        time.sleep(2) 
    elif opcao == '3':
        print("=== Alterar Pessoa ===")
        id = input('Digite o código da pessoa: ')
        nome = input('Digite o nome: ')
        email = input('Digite o email: ')
        fone = input('Digite o fone: ')
        atualizar_pessoa(id, nome, email,fone)
        print("Pessoa atualizado com sucesso!")
        time.sleep(2) 
    elif opcao == '4':
        print("=== Excluir Pessoa === ")        
        id = input('Digite o código do pessoa: ')
        excluir_pessoa(id)
        print(ler_pessoa(id))
        print("Pessoa excluído com sucesso!")
        time.sleep(2) 
    elif opcao == '5':
        print("=== Boletim === ") 
        id = input('Digite o código do aluno: ')
        #Ler duas notas da tela
        n1 = float(input('Digite a nota 1: '))
        n2 = float(input('Digite a nota 2: '))
        freq = float(input('A frequencia do aluno: '))
        #Calcular a média
        media = (n1+n2) / 2
        #Comando condicional - iguais
        if (media >= 7):
            conceito = 'Aprovado'
            print('Aprovado! Média = ',round(media,1))
        else:
            conceito = 'Reprovado'
            print('Reprovado! Média = ',round(media,1))
        
        #Inserir o boletim do aluno
        inserir_boletim(id,n1, n2, freq,media,conceito)
        print('Boletim inserido com sucesso!')
        print(ler_boletim())
        time.sleep(2) 
    elif opcao == '6':
        print('=== Alunos ===')
        dados_pessoa = mostrar_alunos()
        for pessoa in dados_pessoa:
            print(pessoa)
        time.sleep(2)
    elif opcao == '7':
        print('=== Pessoas ===')
        dados_pessoa = ler_pessoas()
        for pessoa in dados_pessoa:
            print(pessoa)
        time.sleep(5)    
    elif opcao == '8':
        print('=== Boletim ===')
        id = input('Digite o código do aluno: ')
        dados_pessoa = mostrar_boletim(id)
        for pessoa in dados_pessoa:
            print(pessoa)
        time.sleep(2)  
    elif opcao == '10':
        criar_turma()
        time.sleep(2)
    elif opcao == '11':
        nome = input('Digite o nome da turma: ')
        dados_turma = ler_turma(nome)
        for turma in dados_turma:
            print(turma)
        time.sleep(2)             
    elif opcao == '9':
        print("Encerrando!") 
        time.sleep(2)          
    else:
        print("Opção inválida. Tente novamente")


#fechar o banco de dados
conn.close()
