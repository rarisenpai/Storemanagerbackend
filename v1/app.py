'''Using Flask to create a REST api with endpoints to fetch and post data.
It uses flask_httpauth to authenticate and offer permissions depending on your role'''

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from v1.users import users, roles
from v1.products import products
from v1.sales import sales

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    '''verify login'''
    for user in users:
        if username in user and check_password_hash(user.get(username), password):
            return username

@auth.get_user_roles
def get_user_roles(username):
    '''get roles'''
    for role in roles:
        return role.get(username)
...

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

@app.route('/api/v1/users')
@auth.login_required(role='admin')
def list_users():
    '''gets all users'''
    return jsonify(users)

@app.route('/api/v1/roles')
@auth.login_required(role='admin')
def list_roles():
    '''gets all roles'''
    return jsonify(roles)

@app.route('/api/v1/newuser', methods=['POST'])
@auth.login_required(role='admin')
def create_user():
    '''Creates a new user'''
    new = request.get_json()
    users.append(new)
    return new

@app.route('/api/v1/newrole', methods=['POST'])
@auth.login_required(role='admin')
def create_role():
    '''Creates a new role'''
    new = request.get_json()
    roles.append(new)
    return new
