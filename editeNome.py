from dicProdutos import produtos

def editeNome():
    codigo = int(input('Digite o codigo do produto que deseja editar: '))
    if codigo in list(produtos.keys()):
        editar = input(f'Deseja editar o produto:  {produtos[codigo][0]}? S/N: ').upper().strip()
        if editar in 'SS':
            nomeAlterado = input('Digite o nome: ')
            produtos[codigo][0] = nomeAlterado
            print('nome alterado com sucesso!')
            print('')
    else:
        print('codigo invalido')
        print('')

