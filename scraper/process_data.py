"""
Main processing script that combines scraping, cleaning, and brand detection

Product Data Processing Tool - Developer Test Assignment
Developed by Sanchit Kathpalia
LinkedIn: https://www.linkedin.com/in/sanchit-kathpalia-a841b5252/
"""
import json
import os
import sys

# Add current directory to path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Import from local modules
from scraper import scrape_products
from data_cleaning import clean_products
from brand_detection import add_brand_to_products

def main():
    """Main processing pipeline"""
    print("=" * 60)
    print("Product Data Processing Pipeline")
    print("=" * 60)
    
    # Step 1: Scrape products
    print("\n[Step 1] Scraping products...")
    products = scrape_products(max_products=100)
    
    # Step 2: Clean products
    print("\n[Step 2] Cleaning product data...")
    cleaned_products = clean_products(products)
    
    # Step 3: Detect brands
    print("\n[Step 3] Detecting brands...")
    final_products = add_brand_to_products(cleaned_products)
    
    # Save final output
    os.makedirs('../data', exist_ok=True)
    output_file = '../data/products_final.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(final_products, f, indent=2, ensure_ascii=False)
    
    print(f"\n[Complete] Saved {len(final_products)} products to {output_file}")
    
    # Print summary
    print("\n" + "=" * 60)
    print("Summary:")
    print("=" * 60)
    brand_counts = {}
    for product in final_products:
        brand = product.get('brand', 'Unknown')
        brand_counts[brand] = brand_counts.get(brand, 0) + 1
    
    print("\nBrand Distribution:")
    for brand, count in sorted(brand_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {brand}: {count}")
    
    print("\nSample Products:")
    for i, product in enumerate(final_products[:5], 1):
        print(f"\n{i}. {product.get('name', 'N/A')}")
        print(f"   Brand: {product.get('brand', 'N/A')}")
        print(f"   Price: {product.get('price', 'N/A')}")
        print(f"   Volume: {product.get('volume_weight', 'N/A')}")

if __name__ == '__main__':
    main()

