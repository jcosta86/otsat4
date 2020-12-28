from flask import Flask, render_template

from funcoes import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', nome='olist', lista=menu)


@app.route('/marketplaces')
def show_marketplaces():
    lista = list_marketplaces()
    return render_template('marketplaces.html', nome='olist', lista=lista, links=links)


@app.route('/categorias')
def show_categories():
    lista = list_categories()
    return render_template('categorias.html', nome='olist', lista=lista, links=links)


@app.route('/subcategorias')
def show_subcategories():
    lista = lista_subcategories()
    return render_template('subcategorias.html', nome='olist', lista=lista, links=links)


app.run(debug=True)
