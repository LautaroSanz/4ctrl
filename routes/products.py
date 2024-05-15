from flask import Blueprint, render_template, request, flash, redirect, url_for
from models import Productos
from app import db  

products = Blueprint('products', __name__)

@products.route('/')
def home():
    productos= Productos.query.all()
    return render_template("index.html",productos=productos)

@products.route('/add_products', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        nombre = request.form['nombre']
        marca = request.form['marca']
        precio = request.form['precio']
        new_product = Productos(nombre=nombre, marca=marca, precio=precio)
        db.session.add(new_product)
        db.session.commit()
        flash('Product Added')
        return redirect(url_for('products.home'))  # Asegúrate de tener una ruta llamada 'index.html' en tu aplicación

@products.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    product = Productos.query.get_or_404(id)  # Corregido para usar el modelo Product en lugar de Productos
    if request.method == 'POST':
        product.nombre = request.form['nombre']
        product.marca = request.form['marca']
        product.precio = request.form['precio']
        db.session.commit()
        flash('Product Updated')
        return redirect(url_for('products.home'))  # Corregido para redirigir a la vista principal del blueprint 'products'
    return render_template('edit-product.html', product=product)


@products.route('/delete/<int:id>', methods=['POST'])
def delete_product(id):
    product = Productos.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    flash('Product Removed Succesfully')
    return redirect(url_for('products.home'))  # Asegúrate de tener una ruta llamada 'index.html' en tu aplicación
