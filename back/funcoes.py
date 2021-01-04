from datetime import datetime

from back.marketplace import Marketplace
from back.category import Category
from back.subcategory import Subcategory
from back.historico import *

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
# salvar_historico(subcategories, 'subcategories_json.txt')
subcategories = {
    'name': 'Radio',
    'products': ['Pionner Auto', 'JBL']
}
# salvar_historico(subcategories, 'subcategories_json.txt')


categories = {
    'name': 'Eletronicos',
    'subcatecories': ['Tv', 'Radio']
}
# salvar_historico(categories, 'categories_json.txt')
categories = {
    'name': 'Suplementos',
    'subcatecories': ['Whey Protein', 'Creatina']
}
# salvar_historico(categories, 'categories_json.txt')


marketplaces = {
    'name': 'Magazine Luiza',
    'categories': ['Eletronicos', 'Cozinha']
}
# salvar_historico(marketplaces)

marketplaces = {
    'name': 'Mercado Livre',
    'categories': ['Eletronicos', 'Suplementos']
}
# salvar_historico(marketplaces, 'teste.txt')

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
     'rota': '/subcategorias'},
    {'nome': 'Log de uso',
     'rota': '/historico'}
]


def salva_log_de_uso(nome_log: str) -> None:
    data_e_hora_atual = datetime.now()
    data_e_hora = data_e_hora_atual.strftime('%d/%m/%Y %H:%M:%S')
    linha_de_log = f'log: {nome_log} - Data e hora: {data_e_hora}'
    salvar_historico(linha_de_log, 'back/arquivos_de_dados/historico_log.txt')


def salva_marketplace(mkt_place: Marketplace) -> None:
    marketplace = f"{'name':{mkt_place.get_name()},'categories': {mkt_place.get_categories()}}"
    salvar_historico(marketplace, 'back/arquivos_de_dados/marketplace_json.txt')
    salva_log_de_uso('salva_marketplace')


def cria_markeplace(name: str, categories_: list) -> Marketplace:
    mkt_plc = Marketplace(name, categories_)
    salva_log_de_uso('cria_marketplace')
    return mkt_plc


def list_marketplaces() -> list:
    lista_marketplaces = ler_historico('back/arquivos_de_dados/marketplace_json.txt')
    salva_log_de_uso('list_marketplace')
    return lista_marketplaces


def list_categories() -> list:
    lista_categorias = ler_historico('back/arquivos_de_dados/categories_json.txt')
    salva_log_de_uso('list_categories')
    return lista_categorias


def lista_subcategories() -> list:
    list_subcategories = ler_historico('back/arquivos_de_dados/subcategories_json.txt')
    salva_log_de_uso('list_subcategories')
    return list_subcategories

def lista_historico() -> list:
    lista = ler_log('back/arquivos_de_dados/historico_log.txt')
    salva_log_de_uso('lista_historico')
    return lista