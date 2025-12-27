"""
Brand detection module
Detects brands from product names using a hardcoded brand list

Product Data Processing Tool - Developer Test Assignment
Developed by Sanchit Kathpalia
LinkedIn: https://www.linkedin.com/in/sanchit-kathpalia-a841b5252/
"""
import re

# Hardcoded brand list
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

def detect_brand(name):
    """
    Detect brand from product name
    Returns brand name if found, "Unknown" otherwise
    """
    if not name:
        return "Unknown"
    
    name_lower = name.lower()
    
    # Check each brand (case-insensitive)
    for brand in BRANDS:
        brand_lower = brand.lower()
        
        # Exact match or brand appears in name
        if brand_lower in name_lower:
            # Return the original brand name (with proper casing)
            return brand
    
    return "Unknown"

def add_brand_to_products(products):
    """
    Add brand detection to a list of products
    """
    for product in products:
        product_name = product.get('name', '') or product.get('original_name', '')
        product['brand'] = detect_brand(product_name)
    
    return products

def main():
    """Test brand detection"""
    test_names = [
        "Coca Cola Original Taste 330ml",
        "Pepsi Max 500ml Bottle",
        "Red Bull Energy Drink 250ml",
        "Lucozade Energy Original 500ml",
        "Some Unknown Product 200ml",
        "Fanta Orange 330ml",
        "Sprite Lemon Lime",
    ]
    
    print("Brand Detection Test:")
    print("-" * 50)
    for name in test_names:
        brand = detect_brand(name)
        print(f"{name:40} -> {brand}")

if __name__ == '__main__':
    main()

