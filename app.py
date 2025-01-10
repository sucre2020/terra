from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/submit_contact')
def submit_contact():
    return render_template('submit_contact.html')

@app.route('/stories_projects')
def stories_projects():
    return render_template('stories_projects.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True)
