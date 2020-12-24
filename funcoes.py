from marketplace import Marketplace
from category import Category
from subcategory import Subcategory


mag_lu = Marketplace('Magazine Luiza', ['Eletronicos', 'Cozinha'])
meli = Marketplace('Mercado Livre', ['Eletronicos', 'Suplementos'])

eletronicos = Category('Eletronicos', ['Tv', 'Radio'])
suplementos = Category('Suplementos', ['Whey'])

tv = Subcategory('Televisor', ['Tv LG 42"', "Tv Sony Bravia"])
radio = Subcategory("Radio", ['Pionner Auto', 'JBL'])
whey = Subcategory('Whey Protein', ['Universal', 'On Nutrition'])

subcategories = [
    {
        'name': tv,
        'id': 1
    },
    {
        'name': radio,
        'id': 2
    },
    {
        'name': whey,
        'id': 3
    },
]


categories = [
    {
        'name': eletronicos,
        'id': 1
    },
    {
        'name': suplementos,
        'id': 2
    }
]

marketplaces = [
    {
        'name': mag_lu,
        'id': 1
    },
    {
        'name': meli,
        'id': 2
    }
]

links = [
    {
        'rota': '/',
        'nome': 'Voltar'
    },
    {
        'rota': 'http://www.olist.com',
        'nome': 'olist'
    }
]

menu = [
    {'nome': 'Marketplaces',
     'rota': '/marketplaces'},
    {'nome': 'Categorias',
     'rota': '/categorias'},
    {'nome': 'Subcategorias',
     'rota': '/subcategorias'}
]





#def lista_nome_marketplaces() -> list:
#    marketplace_names = []
#    for i in marketplaces:
#        name = i['name'].get_name()
#        marketplace_names.append(name)
#    return marketplace_names


def lista_categorias_por_marketplace() -> list:
    return marketplaces


def lista_categorias() -> list:
    return categories


def list_subcategories() -> list:
    return subcategories
