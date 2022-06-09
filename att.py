from flask import Flask,request
app = Flask(__name__)

...
in_memory_datastore = {
   "rice": {"name": "RICE", "Category": "Food", "Quantity": 348},
   "sunglasses": {"name": "SUNGLASSES", "Category": "Fashion", "Quantity": 324},
   "milkshake": {"name": "MILKSHAKE", "Category": "Drinks", "Quantity": 431},
   "scarf": {"name": "SCARF", "Category": "Clothing","Quantity": 312},
   "cakes": {"name": "CAKES", "Category": "Food", "Quantity": 234},
   "beans": {"name": "BEANS", "Category": "Food", "Quantity": 343},
   "coffee": {"name": "COFFEE", "Category": "Drinks", "Quantity": 312},
   "sportshoes": {"name": "SPORTSHOES", "Category":"Sportswear","Quantity": 214},
   "soda": {"name": "SODA", "Category": "Drinks", "Quantity": 341},
   "shirt": {"name": "SHIRT", "Category":"Clothing", "Quantity": 112},
}



@app.route('/api/v1/products')
def list_products():
    return {'products': list(in_memory_datastore.values())}

@app.route('/api/v1/products/<productsId>')
def get_products(productsId):
    return in_memory_datastore[productsId]