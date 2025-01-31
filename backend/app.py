from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/products')
def get_products():
    # Replace with real affiliate data (e.g., from an API)
    products = [
        {"name": "Python Course", "url": "https://example.com/affiliate-link-1"},
        {"name": "Fitness Gear", "url": "https://example.com/affiliate-link-2"}
    ]
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)