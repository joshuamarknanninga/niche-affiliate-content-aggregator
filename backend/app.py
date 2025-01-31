from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for development

# Load affiliate products from a JSON file (create products.json)
AFFILIATE_PRODUCTS = [
    {
        "id": 1,
        "title": "Complete Python Bootcamp",
        "description": "Learn Python programming from scratch",
        "url": "https://example.com/python-course?ref=YOUR_ID",
        "category": "programming",
        "price": "$89.99"
    },
    {
        "id": 2,
        "title": "Premium Yoga Mat",
        "description": "Eco-friendly non-slip yoga mat",
        "url": "https://example.com/yoga-mat?ref=YOUR_ID",
        "category": "fitness",
        "price": "$49.99"
    }
]

@app.route('/api/products', methods=['GET'])
def get_products():
    """Return all products"""
    return jsonify({
        "success": True,
        "count": len(AFFILIATE_PRODUCTS),
        "products": AFFILIATE_PRODUCTS
    })

@app.route('/api/products/<string:category>', methods=['GET'])
def get_products_by_category(category):
    """Filter products by category"""
    filtered_products = [p for p in AFFILIATE_PRODUCTS if p['category'].lower() == category.lower()]
    
    return jsonify({
        "success": True,
        "count": len(filtered_products),
        "category": category,
        "products": filtered_products
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)