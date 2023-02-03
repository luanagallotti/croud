from dicProdutos import produtos

def visualizar():
    for codigo in produtos:
        print(f'Nome {produtos[codigo][0]}, valor R$ {produtos[codigo][1]}, quantidade = {produtos[codigo][2]}')