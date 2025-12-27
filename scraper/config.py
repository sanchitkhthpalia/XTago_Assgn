"""
Configuration file for scraper and data processing
"""
import os

# Scraper settings
SCRAPER_CONFIG = {
    'base_url': 'https://www.wegetanystock.com/',
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

