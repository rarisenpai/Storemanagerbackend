import requests

def test_get_products():
    response = requests.get("http://127.0.0.1:5000/api/v1/products")
    assert response.status_code == 201
    
def test_get_products():
    response = requests.get("http://127.0.0.1:5000/api/v1/products")
    assert response.status_code == 200
    
def test_get_sales():
    response = requests.get("http://127.0.0.1:5000/api/v1/sales")
    assert response.status_code == 201
    
def test_get_sales():
    response = requests.get("http://127.0.0.1:5000/api/v1/sales")
    assert response.status_code == 200
    
def test_get_users():
    response = requests.get("http://127.0.0.1:5000/api/v1/users")
    assert response.status_code == 201
    
def test_get_roles():
    response = requests.get("http://127.0.0.1:5000/api/v1/roles")
    assert response.status_code == 201
    
def test_get_roles():
    response = requests.get("http://127.0.0.1:5000/api/v1/roles")
    assert response.status_code == 200
    



    