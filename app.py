from flask import Flask, render_template, url_for,request
import sqlite3
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

# Initialize the Flask app and SQLAlchemy
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    subcategory = db.Column(db.String(50), nullable=False)
    product_title = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Product {self.product_title}>'

# Create the database and the table (if they don't exist)
with app.app_context():
    db.create_all()


@app.template_filter('static_url')
def static_url(filename):
    return url_for('static', filename=filename)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    page = request.args.get('page', 1, type=int)
    gender = request.args.get('gender')
    subcategories = request.args.getlist('subcategory')

    # Base query
    query = Product.query

    # Apply filters
    if gender:
        query = query.filter(Product.gender == gender)
    if subcategories:
        query = query.filter(Product.subcategory.in_(subcategories))

    # Paginate results
    products = query.paginate(page=page, per_page=12)

    return render_template('products.html', products=products)


@app.route('/login')
def login():
    return '<h2>Login!!!</h2>'

if __name__ == '__main__':
    app.run(debug=True)
