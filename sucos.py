def listar_sucos(frutas):
    i = 1
    for fruta in frutas:
        print(i,' - ',fruta)
        i += 1
    
def criar_pedido():
    
    print('Pedido criado com sucesso!')

def fechar():
    print('Fechar conta!')

#Principal - Tuplas
frutas = ("maçã", "banana", "laranja",'morango','uva')
print(frutas)
# Concatenação de tuplas
frutas = frutas + ("coco", "pessego","abacaxi com hortelã")
#Escrever os valores da tupla
listar_sucos(frutas)
print('=== Loja de Sucos ESP === ')
opcao = ''
while(opcao != '9'):
    print('Operações: 1 - Pedido, 2 - Listar Sucos, 3 - Fechar Conta  9 - Sair')
    opcao = input('Digite a operação: ')
    #Leia da tela
    if(opcao =='1'):
       criar_pedido();
    elif (opcao == '2'):
        listar_sucos(frutas)
    elif (opcao == '3'):
        fechar(frutas)    
    elif(opcao == '9'): 
        print('Encerrando atendimento...')
    else:
        print('Operação inválida')          