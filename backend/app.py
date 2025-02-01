from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import sqlite3
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Rate limiting setup
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Database configuration
DATABASE = 'affiliate.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with app.app_context():
        conn = get_db_connection()
        conn.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                url TEXT NOT NULL,
                category TEXT NOT NULL,
                price TEXT
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS clicks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                timestamp TEXT NOT NULL,
                ip_address TEXT NOT NULL,
                user_agent TEXT,
                FOREIGN KEY (product_id) REFERENCES products (id)
            )
        ''')
        conn.commit()
        conn.close()

# Initialize database tables
init_db()

# Mock affiliate products (replace with real data)
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
    filtered_products = [p for p in AFFILIATE_PRODUCTS 
                       if p['category'].lower() == category.lower()]
    
    return jsonify({
        "success": True,
        "count": len(filtered_products),
        "category": category,
        "products": filtered_products
    })

@app.route('/api/track/<int:product_id>', methods=['POST'])
@limiter.limit("10/minute")  # Prevent click spam
def track_click(product_id):
    """Track affiliate link clicks"""
    try:
        conn = get_db_connection()
        click_data = {
            'product_id': product_id,
            'timestamp': datetime.utcnow().isoformat(),
            'ip_address': request.remote_addr,
            'user_agent': request.headers.get('User-Agent')
        }

        conn.execute('''
            INSERT INTO clicks (product_id, timestamp, ip_address, user_agent)
            VALUES (?, ?, ?, ?)
        ''', (click_data['product_id'], 
              click_data['timestamp'],
              click_data['ip_address'],
              click_data['user_agent']))
        
        conn.commit()
        conn.close()

        return jsonify({
            "success": True,
            "message": "Click tracked",
            "product_id": product_id
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/analytics', methods=['GET'])
def get_analytics():
    """Get basic click analytics"""
    try:
        conn = get_db_connection()
        
        # Total clicks
        total_clicks = conn.execute('SELECT COUNT(*) FROM clicks').fetchone()[0]
        
        # Popular products
        popular_products = conn.execute('''
            SELECT product_id, COUNT(*) as clicks 
            FROM clicks 
            GROUP BY product_id 
            ORDER BY clicks DESC 
            LIMIT 5
        ''').fetchall()

        conn.close()

        return jsonify({
            "success": True,
            "total_clicks": total_clicks,
            "popular_products": [dict(row) for row in popular_products]
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    init_db()  # Ensure tables exist
    app.run(host='0.0.0.0', port=5001, debug=True)