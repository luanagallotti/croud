from dicProdutos import produtos

def excluir():
    codigo = int(input('Digite o codigo do produto que deseja excluir: '))
    if codigo in list(produtos.keys()):
        validacao = input(f'Deseja excluir o produto {produtos[codigo][0]}? S/N: ').upper().strip()
        if validacao in 'Ss':
            del produtos[codigo]
            print('produto excluido com sucesso!')
            print('')
    else:
        print('codigo invalido! ')
        print('')