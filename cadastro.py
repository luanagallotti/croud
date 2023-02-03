from dicProdutos import produtos

def cadastrar():
    print('***Adicionando Produto!***')

    cod = int(input('Cod de Barras: '))
    nome = input('Nome: ')
    valor = float(input('Valor: '))
    qt = int(input('Quantidade: '))
    print('')

    listaProdutos = [nome, valor, qt]
    produtos[cod] = listaProdutos

    return produtos