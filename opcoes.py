from visualizacao import visualizar
from edicao import editar
from exclusao import excluir
from cadastro import cadastrar
from compras import *



def opcoes():
    while True:
        print('Digite 1 para cadastrar produtos')
        print('Digite 2 para excluir')
        print('Digite 3 para editar')
        print('Digite 4 para visualizar cadastro')
        print('Digite 5 para vender')
        print('Digite 0 para encerrar')
        opcao = int(input(': '))

        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            excluir()
        elif opcao == 3:
            editar()
        elif opcao == 4:
            visualizar()
        elif opcao == 5:
            vender()
        elif opcao == 0:
            break
        else:
            print('Opção invalida')



