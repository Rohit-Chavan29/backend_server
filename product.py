from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/products', methods=['GET'])
def get_products():
    products = [
        {"id": 1, "name": "Laptop", "price": 1500},
        {"id": 2, "name": "Smartphone", "price": 800}
    ]
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
