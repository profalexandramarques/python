class Livro():
    #Construtor
    def __init__(self, titulo, autor, ano, isbn):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.isbn = isbn
        #Atributos privado
        self._reservado = False
        self._pessoa = '' 


    #Reservar 
    def reservar(self, pessoa):
       if(not self._reservado):
          self._pessoa = pessoa 
          self._reservado = True
          print('Livro reservado com sucesso!')
       else:
          print('Livro já está reservado!')

    #Devolver
    def devolver(self):
       if(self._reservado):
          self._pessoa = '' 
          self._reservado = False
          print('Livro devolvido com sucesso!')
       else:
          print('Livro não estava reservado!')