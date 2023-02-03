from dicProdutos import produtos
def editeQt():
    codigo = int(input('Digite o codigo do produto que deseja editar: '))
    if codigo in list(produtos.keys()):
        editar = input(f'Deseja editar a quantidade do produto:  {produtos[codigo][0]}? S/N: ').upper().strip()
        if editar in 'SS':
            qtAlterado = input('Digite a nova quantidade: ')
            produtos[codigo][2] = qtAlterado
            print('qt alterada com sucesso!')
            print('')
    else:
        print('codigo invalido')
        print('')