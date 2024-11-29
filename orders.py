from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/orders', methods=['GET'])
def get_orders():
    orders = [
        {"id": 101, "product_id": 1, "quantity": 2},
        {"id": 102, "product_id": 2, "quantity": 1}
    ]
    return jsonify(orders)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
