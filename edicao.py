
def editar():
    print('***Edição de Produtos***')
    print('1 para editar nome: ')
    print('2 para editar valor:')
    print('3 para editar quantidade: ')
    opcao = int(input(': '))
    print('')
    if opcao == 1:
        editeNome()
    elif opcao == 2:
        editeValor()
    elif opcao == 3:
        editeQt()
