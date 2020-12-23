from flask import Flask

from funcoes import *

app = Flask(__name__)


@app.route('/')
def index():
    h1 = '<h1>olist</h1>'
    ol = '''
            <ol> 
                <li><a href='/marketplaces'>Marketplaces</a></li>
                <li><a href='/categorias'>Categorias</a></li>
                <li><a href='/subcategorias'>Subcategorias</a></li>
            </ol>
          '''
    return f'{h1} {ol}'


@app.route('/marketplaces')
def show_marketplaces():
    voltar = "<a href='/'>Voltar</a>"
    return f'{lista_categorias_por_marketplace()} <br/> {voltar}'


@app.route('/categorias')
def show_categories():
    voltar = "<a href='/'>Voltar</a>"
    return f'{lista_categorias()} <br/> {voltar}'


@app.route('/subcategorias')
def show_subcategories():
    voltar = "<a href='/'>Voltar</a>"
    return f'{list_subcategories()} <br/> {voltar}'


app.run(debug=True)
