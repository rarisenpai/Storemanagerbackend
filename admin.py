from att import app

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
    
in_memory_datastore_sales = {"rice":{"RICE":290},
                             "beans":{"BEANS":321},
                             "sunglasses":{"SUNGLASSES":402},
                             "scarves":{"SCARVES":212},
                             "milkshakes":{"MILKSHAKES":232},
                             "sportshoes":{"SPORTSHOES":321},
                             "soda":{"SODA":412},
                             "tea":{"TEA":321},
                             "coffee":{"COFFEE":412},
                             "shirt":{"SHIRT":121}
                             }

if __name__ == '__main__': 
    @app.route('/api/v1/products')
    def list_products():
        return {'products': list(in_memory_datastore.values())}

    @app.route('/api/v1/products/<productsId>')
    def get_products(productsId):
        return in_memory_datastore[productsId]
    @app.route('/api/v1/sales')
    def list_sales():
        return {"Sales": list(in_memory_datastore_sales.values())}

    @app.route('/api/v1/sales/<salesId>')
    def get_sales(salesId):
        return in_memory_datastore_sales[salesId]
