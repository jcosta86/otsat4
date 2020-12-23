from marketplace import Marketplace
from category import Category

mag_lu = Marketplace('Magazine Luiza', ['Eletronicos', 'Cozinha'])
meli = Marketplace('Mercado Livre', ['Eletronicos', 'Suplementos'])

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

eletronicos = Category('Eletronicos', ['Tv', 'Radio'])
suplementos = Category('Suplementos', ['Whey'])

categories = [
    {'nome': eletronicos},
    {'nome': suplementos}
    ]
subcategories = ['Tv', 'Radio', 'Whey', 'Barraca', 'Cadeira dobravel']


def lista_nome_marketplaces() -> list:
    marketplace_names = []
    for i in marketplaces:
        name = i['name'].get_name()
        marketplace_names.append(name)
    return marketplace_names


def lista_categorias_por_marketplace() -> str:
    return marketplaces


def lista_categorias() -> str:
    return categories


def list_subcategories() -> str:
    return subcategories
