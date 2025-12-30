"""
Interactive script to select and scrape from different sites

Product Data Processing Tool - Developer Test Assignment
Developed by Sanchit Kathpalia
LinkedIn: https://www.linkedin.com/in/sanchit-kathpalia-a841b5252/
"""
import sys
import os

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from config import SCRAPING_SITES, SCRAPER_CONFIG
from process_data import main, list_available_sites

def interactive_site_selection():
    """Interactive site selection menu"""
    print("=" * 60)
    print("Product Data Scraper - Site Selection")
    print("=" * 60)
    
    list_available_sites()
    
    print("\nOptions:")
    print("  1. Use default site (wegetanystock)")
    print("  2. Select from available sites")
    print("  3. Enter custom URL")
    print("  4. Exit")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == '1':
        site_key = SCRAPER_CONFIG.get('default_site', 'wegetanystock')
        max_products = input("Max products to scrape (default 100): ").strip()
        max_products = int(max_products) if max_products.isdigit() else 100
        main(site_key=site_key, max_products=max_products)
    
    elif choice == '2':
        print("\nAvailable Sites:")
        enabled_sites = [(k, v) for k, v in SCRAPING_SITES.items() if v.get('enabled', False)]
        for idx, (key, site) in enumerate(enabled_sites, 1):
            print(f"  {idx}. {key} - {site.get('name', 'N/A')}")
        
        site_choice = input("\nEnter site number: ").strip()
        try:
            idx = int(site_choice) - 1
            if 0 <= idx < len(enabled_sites):
                site_key = enabled_sites[idx][0]
                max_products = input("Max products to scrape (default 100): ").strip()
                max_products = int(max_products) if max_products.isdigit() else 100
                main(site_key=site_key, max_products=max_products)
            else:
                print("Invalid selection!")
        except ValueError:
            print("Invalid input!")
    
    elif choice == '3':
        custom_url = input("Enter custom URL to scrape: ").strip()
        if custom_url:
            max_products = input("Max products to scrape (default 100): ").strip()
            max_products = int(max_products) if max_products.isdigit() else 100
            main(site_key='custom', custom_url=custom_url, max_products=max_products)
        else:
            print("URL cannot be empty!")
    
    elif choice == '4':
        print("Exiting...")
        sys.exit(0)
    
    else:
        print("Invalid choice!")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Command line mode
        import argparse
        parser = argparse.ArgumentParser(description='Scrape from different sites')
        parser.add_argument('--site', '-s', help='Site key')
        parser.add_argument('--url', '-u', help='Custom URL')
        parser.add_argument('--max', '-m', type=int, default=100, help='Max products')
        args = parser.parse_args()
        
        main(site_key=args.site, custom_url=args.url, max_products=args.max)
    else:
        # Interactive mode
        interactive_site_selection()

