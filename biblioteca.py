from livro import Livro # type: ignore
import time

#Funções da lista
def cadastrar_livro(livros):
   titulo = input('Digite o título do livro:')
   autor = input('Digite o autor do livro:')
   ano = int(input('Digite o ano do livro:'))
   isbn = input('Digite o ISBN do livro:')
   livro = Livro(titulo,autor, ano, isbn)
   livros.append(livro)
   print('Livro cadastrado com sucesso!')
   time.sleep(5)

#Pesquisar um livro pelo titulo
def pesquisar_livro(titulo,livros):
   achou = False
   i = 0
   livro = None      
   if (len(livros) > 0):
      while (not achou):
        livro = livros[i]   
        print(livro.titulo)
        if(titulo.upper() in livro.titulo.upper()):
            achou = True
        i+=1   
        if (i == len(livros)):
           break
              
   return livro;  

#Pesquisar pelo ISBN
def pesquisar_isbn(isbn,livros):    
   for livro in livros:
      if (livro.isbn == isbn):         
         return livro      
   return None
    
#Listar todos os livros
def listar_livros(livros):
   print('=== Livros ===')
   for livro in livros:
      print(livro.isbn,' - ',livro.titulo)
   print('==============')

#Principal
livros = []
opcao = ''
while(opcao != '9'):
    print('Operações: 1 - Cadastrar Livro')
    print('2 - Pesquisar um livro pelo título, ')
    print('3 - Pesquisar um livro pelo ISBN, ')
    print('4 - Reservar,')
    print('5 - Devolver,')
    print('6 - Listar todos os livros')
    print('9 - Sair')
    opcao = input('Digite a operação: ')
    if(opcao =='1'):  
       cadastrar_livro(livros)
    elif (opcao == '2'):
       titulo = input('Digite o título do livro:')
       livro = pesquisar_livro(titulo,livros)
       if (livro != None):
          print('Título encontrado: ',livro.isbn,' - ',livro.titulo)   
       else:
          print('Título não encontrado!')
       time.sleep(5)
    elif (opcao == '3'):
       isbn = input('Digite o isbn do livro:')
       livro = pesquisar_isbn(isbn,livros)
       if (livro == None):
          print('Título não encontrado!')
       else:
          print('Título encontrado: ',livro.isbn,' - ',livro.titulo)   
       time.sleep(5)
    elif (opcao == '4'):      
       isbn = input('Digite o isbn do livro:')       
       livro = pesquisar_isbn(isbn,livros)
       if (livro != None):
         nome = input('Digite o nome da pessoa:')
         livro.reservar(nome)
       else:
          print('Título não encontrado!')  
       time.sleep(5)
    elif (opcao == '5'):      
       isbn = input('Digite o isbn do livro:')
       livro = pesquisar_isbn(isbn,livros)
       if (livro != None):
         livro.devolver()
       else:
          print('Título não encontrado!')  
       time.sleep(5)   
    elif(opcao == '6'): 
        listar_livros(livros)     
        time.sleep(5)
    elif(opcao == '9'): 
        print('Volte Sempre ...')      
        time.sleep(3)
    else:
        print('Operação inválida')        


       


