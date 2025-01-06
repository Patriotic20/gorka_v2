from ..main import app
from src.model.product import Product
from fastapi.testclient import TestClient

client = TestClient(app)


def test_add(db):
    product_data = {
        "barcode" : "123458",
        "name" : "Ganta",
        "quantity": 80,
    }
    
    response = client.post("/product/add" , json=product_data)
    assert response.status_code == 200
    
    response_data = response.json()
    
    assert response_data["barcode"] == product_data["barcode"]
    assert response_data["name"] == product_data["name"]
    assert response_data["quantity"] == product_data["quantity"]
    
    
def test_find(db):
    response = client.get("/product/find?barcode=123458")
    assert response.status_code == 200
    assert response.json() == {
        "id" : 1,
        "name" : "Ganta",
        "barcode" : "123458",
        "quantity" : 80,
    }
    
def test_update(db):
    update_data = {
        "barcode": "123458",
        "name": "Updated Product",
        "quantity": 20
    }

    response = client.put("product/update", json=update_data)

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["name"] == "Updated Product"
    assert response_data["quantity"] == 20


    # updated_product = db.query(Product).filter_by(barcode="123458").first()
    # assert updated_product.name == "Updated Product"
    # assert updated_product.quantity == 20