from funcoes import *
from historico import ler_historico


def menu() -> int:
    options = ['Marketplaces', 'Categorias', 'Subcategorias', 'Sair']

    print('\n--------  olist  --------\n')

    for i, option in enumerate(options):
        print(f'[{i + 1}] - {option}')

    op_menu = int(input('\nSelecione uma opção: '))
    return op_menu


def listar_itens(list_: list, key_name: str, key_value: str) -> None:
    print()
    for index in range(len(list_)):
        elemento = list_[index]
        print(elemento[key_name])
        for categories in (elemento[key_value]):
            print(' -> ', categories)


while True:
    try:
        op = menu()
        if op == 4:
            print('Até logo!')
            break
        else:
            if op == 1:
                listar_itens(list_marketplaces(), 'name', 'categories')
            elif op == 2:
                listar_itens(list_categories(), 'name', 'subcatecories')
            elif op == 3:
                listar_itens(lista_subcategories(), 'name', 'products')
            else:
                print('Opção inválida.')
    except Exception as e:
        print(e)