'''Using Flask to create a REST api with endpoints to fetch and post data.
It uses flask_httpauth to authenticate and offer permissions depending on your role'''

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "admin": generate_password_hash("admin"),
    "attendant": generate_password_hash("attendant")
}

roles = {
    "admin": "admin",
    "attendant": "attendant"
}

@auth.verify_password
def verify_password(username, password):
    '''verify login'''
    if username in users and check_password_hash(users.get(username), password):
        return username

@auth.get_user_roles
def get_user_roles(username):
    '''get roles'''
    return roles.get(username)
...
products = [
    {"rice": {"name": "RICE", "Category": "Food", "Quantity": 348}},
    {"sunglasses": {"name": "SUNGLASSES", "Category": "Fashion", "Quantity": 324}},
    {"milkshake": {"name": "MILKSHAKE", "Category": "Drinks", "Quantity": 431}},
    {"scarf": {"name": "SCARF", "Category": "Clothing","Quantity": 312}},
    {"cakes": {"name": "CAKES", "Category": "Food", "Quantity": 234}},
    {"beans": {"name": "BEANS", "Category": "Food", "Quantity": 343}},
    {"coffee": {"name": "COFFEE", "Category": "Drinks", "Quantity": 312}},
    {"sportshoes": {"name": "SPORTSHOES", "Category":"Sportswear","Quantity": 214}},
    {"soda": {"name": "SODA", "Category": "Drinks", "Quantity": 341}},
    {"shirt": {"name": "SHIRT", "Category":"Clothing", "Quantity": 112}},
]

sales = [
    {"rice":{"RICE":290}},
    {"beans":{"BEANS":321}},
    {"sunglasses":{"SUNGLASSES":402}},
    {"scarves":{"SCARVES":212}},
    {"milkshakes":{"MILKSHAKES":232}},
    {"sportshoes":{"SPORTSHOES":321}},
    {"soda":{"SODA":412}},
    {"tea":{"TEA":321}},
    {"coffee":{"COFFEE":412}},
    {"shirt":{"SHIRT":121}}
]

@app.route('/')
@auth.login_required
def index():
    '''returns a greeting to the user'''
    return f"Hello, {auth.current_user()}!"

@app.route('/api/v1/products')
@auth.login_required(role=['admin','attendant'])
def list_products():
    '''gets all products'''
    return jsonify(products)

@app.route('/api/v1/products/<productsId>')
@auth.login_required(role=['admin','attendant'])
def get_products(products_id):
    '''gets specific product'''
    for product in products:
        if products_id in product:
            return product[products_id]
        return {'error': 'Product not found'}

@app.route('/api/v1/sales')
@auth.login_required(role='admin')
def list_sales():
    '''gets all sales'''
    return jsonify(sales)

@app.route('/api/v1/sales/<salesId>')
@auth.login_required(role='admin')
def get_sales(sales_id):
    '''gets a specific sale order'''
    for sale in sales:
        if sales_id in sale:
            return sale[sales_id]
        return {'error': 'sale not found'}

@app.route('/api/v1/products', methods=['POST'])
@auth.login_required(role='admin')
def create_product():
    '''Creates a new product'''
    new = request.get_json()
    products.append(new)
    return new

@app.route('/api/v1/sales', methods=['POST'])
@auth.login_required(role=['admin','attendant'])
def create_sales():
    '''creates a new sale order'''
    new = request.get_json()
    sales.append(new)
    return new
