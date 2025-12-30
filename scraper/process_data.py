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
from config import SCRAPING_SITES, SCRAPER_CONFIG

def list_available_sites():
    """List all available scraping sites"""
    print("\nAvailable Scraping Sites:")
    print("-" * 60)
    for key, site in SCRAPING_SITES.items():
        status = "[Enabled]" if site.get('enabled', False) else "[Disabled]"
        print(f"  {key:20} - {site.get('name', 'N/A'):30} {status}")
        if site.get('base_url'):
            print(f"    URL: {site['base_url']}")
    print("-" * 60)

def main(site_key=None, custom_url=None, max_products=100):
    """
    Main processing pipeline
    
    Args:
        site_key: Key from SCRAPING_SITES config (e.g., 'wegetanystock')
        custom_url: Custom URL to scrape (if site_key is 'custom')
        max_products: Maximum number of products to scrape
    """
    print("=" * 60)
    print("Product Data Processing Pipeline")
    print("=" * 60)
    
    # Show available sites if no site specified
    if site_key is None:
        list_available_sites()
        print(f"\nUsing default site: {SCRAPER_CONFIG.get('default_site', 'wegetanystock')}")
        site_key = SCRAPER_CONFIG.get('default_site', 'wegetanystock')
    
    # Step 1: Scrape products
    print(f"\n[Step 1] Scraping products from: {SCRAPING_SITES.get(site_key, {}).get('name', site_key)}...")
    products = scrape_products(max_products=max_products, site_key=site_key, custom_url=custom_url)
    
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
    import argparse
    
    parser = argparse.ArgumentParser(description='Product Data Processing Pipeline')
    parser.add_argument('--site', '-s', type=str, help='Site key to scrape from (e.g., wegetanystock)')
    parser.add_argument('--url', '-u', type=str, help='Custom URL to scrape (use with --site custom)')
    parser.add_argument('--max', '-m', type=int, default=100, help='Maximum number of products to scrape')
    parser.add_argument('--list-sites', '-l', action='store_true', help='List all available sites')
    
    args = parser.parse_args()
    
    if args.list_sites:
        list_available_sites()
    else:
        main(site_key=args.site, custom_url=args.url, max_products=args.max)

