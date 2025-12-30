"""
Flask backend API for web scraping
Allows React frontend to scrape websites via API

Product Data Processing Tool - Developer Test Assignment
Developed by Sanchit Kathpalia
LinkedIn: https://www.linkedin.com/in/sanchit-kathpalia-a841b5252/
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Add scraper directory to path
scraper_dir = os.path.join(os.path.dirname(__file__), '..', 'scraper')
sys.path.insert(0, scraper_dir)

from scraper import scrape_products
from data_cleaning import clean_products
from brand_detection import add_brand_to_products
from config import SCRAPING_SITES

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'message': 'Scraper API is running'})

@app.route('/api/sites', methods=['GET'])
def get_sites():
    """Get list of available scraping sites"""
    sites = []
    for key, site in SCRAPING_SITES.items():
        if site.get('enabled', False):
            sites.append({
                'key': key,
                'name': site.get('name', ''),
                'baseUrl': site.get('base_url', ''),
                'description': site.get('description', '')
            })
    return jsonify({'sites': sites})

@app.route('/api/scrape', methods=['POST'])
def scrape():
    """
    Scrape products from a website
    
    Request body:
    {
        "site": "wegetanystock" or "custom",
        "url": "https://example.com" (required if site is "custom"),
        "maxProducts": 100
    }
    """
    try:
        data = request.get_json()
        
        site_key = data.get('site', 'wegetanystock')
        custom_url = data.get('url', '')
        max_products = data.get('maxProducts', 50)
        
        # Validate input
        if site_key == 'custom' and not custom_url:
            return jsonify({
                'error': 'URL is required when site is "custom"'
            }), 400
        
        if max_products > 200:
            max_products = 200  # Limit to prevent abuse
        
        # Scrape products
        print(f"Scraping from {site_key}: {custom_url if site_key == 'custom' else 'default'}")
        products = scrape_products(
            max_products=max_products,
            site_key=site_key,
            custom_url=custom_url if site_key == 'custom' else None
        )
        
        # Clean products
        cleaned_products = clean_products(products)
        
        # Detect brands
        final_products = add_brand_to_products(cleaned_products)
        
        return jsonify({
            'success': True,
            'products': final_products,
            'count': len(final_products),
            'site': site_key,
            'url': custom_url if site_key == 'custom' else SCRAPING_SITES.get(site_key, {}).get('base_url', '')
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

@app.route('/api/process', methods=['POST'])
def process_products():
    """
    Process product names (cleaning and brand detection)
    Used when user pastes product names directly
    
    Request body:
    {
        "productNames": ["Product 1", "Product 2", ...]
    }
    """
    try:
        data = request.get_json()
        product_names = data.get('productNames', [])
        
        if not product_names:
            return jsonify({
                'error': 'productNames array is required'
            }), 400
        
        # Create product objects
        products = [{'name': name, 'original_name': name} for name in product_names]
        
        # Clean products
        cleaned_products = clean_products(products)
        
        # Detect brands
        final_products = add_brand_to_products(cleaned_products)
        
        # Format for frontend
        result = []
        for product in final_products:
            result.append({
                'originalName': product.get('original_name', product.get('name', '')),
                'cleanedName': product.get('name', ''),
                'detectedBrand': product.get('brand', 'Unknown'),
                'price': product.get('price', ''),
                'volumeWeight': product.get('volume_weight', '')
            })
        
        return jsonify({
            'success': True,
            'products': result,
            'count': len(result)
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("Starting Scraper API Server...")
    print(f"API will be available at http://0.0.0.0:{port}")
    print("Endpoints:")
    print("  GET  /api/health - Health check")
    print("  GET  /api/sites - List available sites")
    print("  POST /api/scrape - Scrape from website")
    print("  POST /api/process - Process product names")
    # Always bind to 0.0.0.0 for deployment platforms
    app.run(host='0.0.0.0', port=port, debug=False, threaded=True)

