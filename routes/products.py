from flask import Blueprint, render_template, request, redirect, url_for, session, flash

products_bp = Blueprint('products', __name__)

products = [
    {
        "name": "Goat",
        "price": 50000,
        "description": "Healthy farm goat",
        "image": "/static/images/farm1.webp",
        "gender_options": ["Male", "Female"],
        "color_options": ["Brown", "White", "Black"],
    },
    {
        "name": "Pig",
        "price": 120000,
        "description": "Well-fed pig for farming",
        "image": "/static/images/morePigs.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Pink", "Brown", "Black"],
    },
    {
        "name": "Turkey",
        "price": 55000,
        "description": "Well-bred Turkey for farming",
        "image": "/static/images/turkeyFarming.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Brown","Black", "White"],
    },
    {
        "name": "Sheep",
        "price": 75000,
        "description": "Well-bred Sheep for farming",
        "image": "/static/images/farm3.webp",
        "gender_options": ["Male", "Female"],
        "color_options": ["Brown","Black", "White"],
    },
    {
        "name": "Snail",
        "price": 15000,
        "description": "Well-bred Snails for farming",
        "image": "/static/images/snailFarm.webp",
        "gender_options": ["Male", "Female"],
        "color_options": ["Brown","Black", "White"],
    }
]

@products_bp.route('/products')
def show_products():
    cart = session.get('cart', [])
    cart_item_count = sum(item['quantity'] for item in cart)
    return render_template('products.html', products=products, cart_item_count=cart_item_count)

@products_bp.route('/cart', methods=['POST'])
def cart():
    item = {
        "name": request.form.get("name"),
        "price": int(request.form.get("price")),
        "gender": request.form.get("gender"),
        "color": request.form.get("color"),
        "quantity": 1
    }
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(item)
    session.modified = True
    flash(f"{item['name']} added to cart!")
    return redirect(url_for('products.show_products'))

@products_bp.route('/cart',)
def view_cart():
    cart = session.get('cart', [])
    return render_template('cart.html', cart=cart)

@products_bp.route('/update-cart/<name>', methods=['POST'])
def update_cart(name):
    cart = session.get('cart', [])
    new_quantity = int(request.form.get('quantity', 1))
    for item in cart:
        if item['name'] == name:
            item['quantity'] = new_quantity
            break
    session['cart'] = cart
    session.modified = True
    flash(f"Quantity updated for {name}.")
    return redirect(url_for('products.view_cart'))

@products_bp.route('/remove-from-cart/<name>', methods=['POST'])
def remove_from_cart(name):
    cart = session.get('cart', [])
    cart = [item for item in cart if item['name'] != name]
    session['cart'] = cart
    session.modified = True
    flash(f"{name} removed from cart.")
    return redirect(url_for('products.view_cart'))
