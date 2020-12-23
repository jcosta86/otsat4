from funcoes import *


def menu() -> int:
    options = ['Marketplaces', 'Categorias', 'Subcategorias', 'Sair']

    print('\n--------  olist  --------\n')

    for i, option in enumerate(options):
        print(f'[{i + 1}] - {option}')

    op_menu = int(input('\nSelecione uma opção: '))
    return op_menu


while True:
    try:
        op = menu()
        if op == 4:
            print('Até logo!')
            break
        else:
            if op == 1:
                lista_categorias_por_marketplace()
            elif op == 2:
                lista_categorias()
            elif op == 3:
                list_subcategories()
            else:
                print('Opção inválida.')
    except Exception as e:
        print(e)
