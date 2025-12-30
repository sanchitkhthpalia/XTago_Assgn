"""
Configuration file for scraper and data processing
"""
import os

# Available scraping sites configuration
SCRAPING_SITES = {
    'wegetanystock': {
        'name': 'We Get Any Stock',
        'base_url': 'https://www.wegetanystock.com/',
        'category_paths': ['/category/drinks', '/category/beverages', '/category/food', '/products', '/shop'],
        'product_selectors': [
            {'tag': 'div', 'class': 'product'},
            {'tag': 'div', 'class': 'product-item'},
            {'tag': 'div', 'class': 'product-card'},
        ],
        'enabled': True,
    },
    'books_toscrape': {
        'name': 'Books to Scrape',
        'base_url': 'http://books.toscrape.com/',
        'category_paths': ['/catalogue/category/books_1/index.html'],
        'product_selectors': [
            {'tag': 'article', 'class': 'product_pod'},
            {'tag': 'article', 'class': 'product'},
        ],
        'enabled': True,
    },
    'quotes_toscrape': {
        'name': 'Quotes to Scrape',
        'base_url': 'http://quotes.toscrape.com/',
        'category_paths': [],
        'product_selectors': [
            {'tag': 'div', 'class': 'quote'},
        ],
        'enabled': True,
    },
    'scrapethissite': {
        'name': 'Scrape This Site',
        'base_url': 'https://www.scrapethissite.com/',
        'category_paths': ['/pages/'],
        'product_selectors': [
            {'tag': 'div', 'class': 'page'},
        ],
        'enabled': True,
    },
    'amazon': {
        'name': 'Amazon (Example)',
        'base_url': 'https://www.amazon.co.uk/',
        'category_paths': ['/s?k=beverages', '/s?k=drinks'],
        'product_selectors': [
            {'tag': 'div', 'class': 's-result-item'},
            {'tag': 'div', 'data-component-type': 's-search-result'},
        ],
        'enabled': False,  # Requires JavaScript
    },
    'custom': {
        'name': 'Custom URL',
        'base_url': '',  # Will be provided by user
        'category_paths': [],
        'product_selectors': [
            {'tag': 'div', 'class': 'product'},
            {'tag': 'div', 'class': 'product-item'},
            {'tag': 'article', 'class': 'product'},
        ],
        'enabled': True,
    }
}

# Default scraper settings
SCRAPER_CONFIG = {
    'default_site': 'wegetanystock',  # Default site to scrape
    'max_products': 100,
    'timeout': 10,
    'retry_attempts': 3,
    'delay_between_requests': 1,  # seconds
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}

# Data cleaning settings
CLEANING_CONFIG = {
    'descriptors_to_remove': ['Can', 'Bottle', 'Bar', 'Pack', 'Pk', 'Pkt', 'Packet'],
    'case_style': 'title',  # 'title', 'upper', 'lower', 'original'
}

# Brand list (can be extended)
BRANDS = [
    "Coca-Cola", "Coca Cola", "Coke",
    "Lucozade",
    "Red Bull",
    "Pepsi",
    "Fanta",
    "Sprite",
    "7UP", "7-Up",
    "Tango",
    "Dr Pepper", "Dr. Pepper",
    "Monster",
    "Rockstar",
    "Relentless",
    "Powerade",
    "Gatorade",
    "Ribena",
    "Robinsons",
    "Innocent",
    "Tropicana",
    "Ocean Spray",
    "Volvic",
    "Evian",
    "Highland Spring",
]

# Output settings
OUTPUT_CONFIG = {
    'data_dir': '../data',
    'raw_file': 'products_raw.json',
    'cleaned_file': 'products_cleaned.json',
    'final_file': 'products_final.json',
    'indent': 2,
    'ensure_ascii': False,
}

# Multipack patterns
MULTIPACK_PATTERNS = [
    (r'(\d+)\s*x\s*(\d+\s*(?:ml|g|l|kg))', r'\1x\2'),  # 6x250ml
    (r'(\d+)\s*x\s*', r'\1x'),  # 6x
    (r'(\d+)\s*pk\b', r'\1pk'),  # 4pk
    (r'(\d+)\s*pack\b', r'\1 Pack'),  # 12 Pack
]

