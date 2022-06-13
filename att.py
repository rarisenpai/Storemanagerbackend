from flask import Flask, request, jsonify
app = Flask(__name__)

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



@app.route('/')
def welcome():
    return '<h1>Hello Attendant</h1>'

@app.route('/api/v1/products')
def list_products():
    return jsonify(products)

@app.route('/api/v1/products/<productsId>')
def get_products(productsId):
    for product in products:
        if productsId in product:
            return product[productsId]
        else:
            return {'error': 'Product not found'}