from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Product API!"})

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products), 200

@app.route("/products/<int:id>")
def get_product_by_id(id):
    for product in products:
        if product["id"] == id:
            return jsonify(product), 200
    return jsonify({"message": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
