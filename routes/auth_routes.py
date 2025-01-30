from flask import Blueprint, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from db.users import create_user, find_user_by_email, render_template


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    hashed_password = generate_password_hash(password)
    
    if find_user_by_email(email):
        flash("Email already exists.")
        return redirect(url_for('auth.register'))
    
    user_id = create_user(name, email, hashed_password)
    flash("Registration successful!")
    session['user_id'] = user_id
    return redirect(url_for('products.show_products'))

@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user = find_user_by_email(email)
    
    if user and check_password_hash(user['password_hash'], password):
        session['user_id'] = str(user['_id'])
        flash("Login successful!")
        return redirect(url_for('products.show_products'))
    else:
        flash("Invalid credentials.")
        return redirect(url_for('auth.login'))
