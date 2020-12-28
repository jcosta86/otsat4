from marketplace import Marketplace
from category import Category
from subcategory import Subcategory
from historico import *

mag_lu = Marketplace('Magazine Luiza', ['Eletronicos', 'Cozinha'])
meli = Marketplace('Mercado Livre', ['Eletronicos', 'Suplementos'])

eletronicos = Category('Eletronicos', ['Tv', 'Radio'])
suplementos = Category('Suplementos', ['Whey'])

tv = Subcategory('Televisor', ['Tv LG 42"', "Tv Sony Bravia"])
radio = Subcategory("Radio", ['Pionner Auto', 'JBL'])
whey = Subcategory('Whey Protein', ['Universal', 'On Nutrition'])

subcategories = {
    'name': 'Televisor',
    'products': ['Tv LG 42"', "Tv Sony Bravia"]
}
#salvar_historico(subcategories, 'subcategories_json.txt')
subcategories = {
    'name': 'Radio',
    'products': ['Pionner Auto', 'JBL']
}
#salvar_historico(subcategories, 'subcategories_json.txt')



categories = {
    'name': 'Eletronicos',
    'subcatecories': ['Tv', 'Radio']
}
#salvar_historico(categories, 'categories_json.txt')
categories = {
    'name': 'Suplementos',
    'subcatecories': ['Whey Protein', 'Creatina']
}
#salvar_historico(categories, 'categories_json.txt')


marketplaces = {
    'name': 'Magazine Luiza',
    'categories': ['Eletronicos', 'Cozinha']
}
# salvar_historico(marketplaces)

marketplaces = {
    'name': 'Mercado Livre',
    'categories': ['Eletronicos', 'Suplementos']
}
#salvar_historico(marketplaces, 'teste.txt')

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


def salva_marketplace(mkt_place: Marketplace) -> None:
    marketplace = f"{'name':{mkt_place.get_name()},'categories': {mkt_place.get_categories()}}"
    salvar_historico(marketplace, 'marketplace_json.txt')


def cria_markeplace(name: str, categories_: list) -> Marketplace:
    mkt_plc = Marketplace(name, categories_)
    return mkt_plc


def list_marketplaces() -> list:
    lista_marketplaces = ler_historico('marketplace_json.txt')
    return lista_marketplaces


def list_categories() -> list:
    lista_categorias = ler_historico('categories_json.txt')
    return lista_categorias


def lista_subcategories() -> list:
    list_subcategories = ler_historico('subcategories_json.txt')
    return list_subcategories
