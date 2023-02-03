from dicProdutos import produtos

def editeValor():
    codigo = int(input('Digite o codigo do produto que deseja editar: '))
    if codigo in list(produtos.keys()):
        editar = input(f'Deseja editar o valor do produto:  {produtos[codigo][0]}? S/N: ').upper().strip()
        if editar in 'SS':
            valorAlterado = input('Digite o novo valor: ')
            produtos[codigo][1] = valorAlterado
            print('valor alterado com sucesso!')
            print('')
    else:
        print('codigo invalido')
        print('')