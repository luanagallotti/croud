from dicProdutos import produtos

def vender ():
    soma = cont = desconto = 0
    while True:
        compra = str(input('deseja efetuar compras? s/n: ')).upper().strip()
        if compra in 'Ss':
            cod = int(input('digite o codigo do produto que deseja comprar: '))
            if cod in list(produtos.keys()):
                qtVender = int(input('Digite a quantidade de produtos a vender: '))
                if qtVender <= produtos[cod][2]:
                    soma += produtos[cod][1] * qtVender
                    produtos[cod][2] -= qtVender
                else:
                    print('quantidade insuficiente!')
                    print(f'estoque: {produtos[cod][2]}')
                    break
            else:
                print('codigo invalido')
                break

        else:
            break
        print(f' valor a pagar {soma}')
        if soma <= 1000:
            desconto = (soma * (5/100))
        elif soma >= 5000:
            desconto = (soma * (10/100))
        else:
            desconto = (soma * (15/100))
        print(f'Valor total R$ {soma}, desconto R$ {desconto}')
        print(f'valor a pagar R$ {soma - desconto}')
        troco = float(input('valor pago pelo cliente: '))
        while troco < (soma - desconto):
                print(f'Valor insuficiente, falta R$ {(soma - desconto) - troco}')
                troco = float(input('valor pago pelo cliente: '))
        else:
            print(f' troco cliente R$ {troco - (soma - desconto)}')






