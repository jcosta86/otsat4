marketplaces = [
    {
        'name': 'Magazine Luiza',
        'id': 1
    },
    {
        'name': 'Mercado Livre',
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

categories = ['Eletronicos', 'Suplementos', 'Camping']
subcategories = ['Tv', 'Radio', 'Whey', 'Barraca', 'Cadeira dobravel']


def lista_categorias_por_marketplace() -> str:
    return marketplaces


def lista_categorias() -> str:
    return categories


def list_subcategories() -> str:
    return subcategories
