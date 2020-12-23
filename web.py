from flask import Flask, render_template

from funcoes import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', nome='olist', lista=menu)


@app.route('/marketplaces')
def show_marketplaces():
    lista = lista_categorias_por_marketplace()
    return render_template('marketplaces.html', nome='olist', lista=lista, links=links)


@app.route('/categorias')
def show_categories():
    return render_template('categorias.html', nome='olist', lista=lista_categorias(), links=links)


@app.route('/subcategorias')
def show_subcategories():
    return render_template('categorias.html', nome='olist', lista=list_subcategories(), links=links)


app.run(debug=True)
