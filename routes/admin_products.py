from flask import Blueprint, render_template, request, flash, redirect, url_for
from db.products import create_product, update_product, delete_product, get_all_products

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/products')
def admin_products():
    products = get_all_products()
    return render_template('admin/products.html', products=products)

@admin_bp.route('/products/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = int(request.form['price'])
        description = request.form['description']
        image = request.form['image']
        gender_options = request.form.getlist('gender_options')
        color_options = request.form.getlist('color_options')
        create_product(name, price, description, image, gender_options, color_options)
        flash(f"Product '{name}' added successfully!")
        return redirect(url_for('admin.admin_products'))
    return render_template('admin/add_product.html')

@admin_bp.route('/products/delete/<name>', methods=['POST'])
def delete_product_route(name):
    if delete_product(name):
        flash(f"Product '{name}' deleted successfully.")
    else:
        flash(f"Failed to delete product '{name}'.")
    return redirect(url_for('admin.admin_products'))
