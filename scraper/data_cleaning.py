"""
Data cleaning module for product data
Handles unit standardization, price cleaning, casing, and descriptor removal

Product Data Processing Tool - Developer Test Assignment
Developed by Sanchit Kathpalia
LinkedIn: https://www.linkedin.com/in/sanchit-kathpalia-a841b5252/
"""
import re
import json
import os

def standardize_units(volume_weight):
    """
    Standardize units: convert "Grams", "G", "g", "ml", "Milliliters" to standard format
    Examples: "500 Grams" -> "500g", "330 ml" -> "330ml"
    """
    if not volume_weight:
        return ""
    
    # Convert to lowercase for processing
    text = volume_weight.strip()
    
    # Pattern to match number followed by unit
    patterns = [
        (r'(\d+)\s*(?:grams?|g)\b', r'\1g'),
        (r'(\d+)\s*(?:milliliters?|ml)\b', r'\1ml'),
        (r'(\d+)\s*(?:liters?|litres?|l)\b', r'\1l'),
        (r'(\d+)\s*(?:kilograms?|kg)\b', r'\1kg'),
    ]
    
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    
    return text.strip()

def clean_price(price):
    """
    Remove price phrases like "PMP £1.25", "PM £1", "£2.00"
    Keep only the actual price value
    """
    if not price:
        return ""
    
    # Remove common price prefixes
    price = re.sub(r'PMP\s*', '', price, flags=re.IGNORECASE)
    price = re.sub(r'PM\s*', '', price, flags=re.IGNORECASE)
    price = re.sub(r'RRP\s*', '', price, flags=re.IGNORECASE)
    
    # Extract price value (keep currency symbol and number)
    price_match = re.search(r'([£$€]?\s*\d+\.?\d*)', price)
    if price_match:
        return price_match.group(1).strip()
    
    return price.strip()

def clean_product_name(name):
    """
    Clean product name by:
    - Standardizing casing to title case
    - Removing unnecessary descriptors (can, bottle, bar, pack, pk)
    - Removing extra spaces
    """
    if not name:
        return ""
    
    # Convert to title case
    name = name.title()
    
    # Remove unnecessary descriptors (case-insensitive)
    descriptors = ['Can', 'Bottle', 'Bar', 'Pack', 'Pk', 'Pkt', 'Packet']
    for descriptor in descriptors:
        # Remove standalone descriptor words
        name = re.sub(r'\b' + re.escape(descriptor) + r'\b', '', name, flags=re.IGNORECASE)
    
    # Remove extra spaces and clean up
    name = ' '.join(name.split())
    
    return name.strip()

def detect_multipack(name):
    """
    Detect multipack patterns like "6x250ml", "4pk", "12 Pack"
    Returns multipack info if found, empty string otherwise
    """
    if not name:
        return ""
    
    # Patterns for multipack detection
    patterns = [
        (r'(\d+)\s*x\s*(\d+\s*(?:ml|g|l|kg))', r'\1x\2'),  # 6x250ml
        (r'(\d+)\s*x\s*', r'\1x'),  # 6x
        (r'(\d+)\s*pk\b', r'\1pk'),  # 4pk
        (r'(\d+)\s*pack\b', r'\1 Pack'),  # 12 Pack
        (r'(\d+)\s*pack\b', r'\1 Pack'),  # 12 pack
    ]
    
    for pattern, replacement in patterns:
        match = re.search(pattern, name, re.IGNORECASE)
        if match:
            return match.group(0).strip()
    
    return ""

def generate_slug(name):
    """
    Generate SEO-friendly slug from cleaned name
    Example: "Coca Cola Zero 330ml" -> "coca-cola-zero-330ml"
    """
    if not name:
        return ""
    
    # Convert to lowercase
    slug = name.lower()
    
    # Replace spaces with hyphens
    slug = slug.replace(' ', '-')
    
    # Remove special characters, keep alphanumeric and hyphens
    slug = re.sub(r'[^a-z0-9-]', '', slug)
    
    # Remove multiple consecutive hyphens
    slug = re.sub(r'-+', '-', slug)
    
    # Remove leading/trailing hyphens
    slug = slug.strip('-')
    
    return slug

def clean_product(product):
    """
    Clean a single product dictionary
    """
    cleaned = product.copy()
    
    # Clean name
    original_name = cleaned.get('name', '')
    cleaned['original_name'] = original_name
    cleaned['name'] = clean_product_name(original_name)
    
    # Clean price
    cleaned['price'] = clean_price(cleaned.get('price', ''))
    
    # Standardize volume/weight
    cleaned['volume_weight'] = standardize_units(cleaned.get('volume_weight', ''))
    
    # Detect multipack
    cleaned['multipack'] = detect_multipack(original_name)
    
    # Generate slug
    cleaned['slug'] = generate_slug(cleaned['name'])
    
    return cleaned

def clean_products(products):
    """
    Clean a list of products
    """
    return [clean_product(p) for p in products]

def main():
    """Main function to clean scraped data"""
    # Load raw products
    input_file = '../data/products_raw.json'
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found. Please run scraper.py first.")
        return
    
    with open(input_file, 'r', encoding='utf-8') as f:
        products = json.load(f)
    
    print(f"Cleaning {len(products)} products...")
    
    # Clean products
    cleaned_products = clean_products(products)
    
    # Save cleaned products
    output_file = '../data/products_cleaned.json'
    os.makedirs('../data', exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_products, f, indent=2, ensure_ascii=False)
    
    print(f"Saved {len(cleaned_products)} cleaned products to {output_file}")
    
    # Print sample
    print("\nSample cleaned products:")
    for i, product in enumerate(cleaned_products[:5]):
        print(f"\n{i+1}. Original: {product.get('original_name', 'N/A')}")
        print(f"   Cleaned: {product.get('name', 'N/A')}")
        print(f"   Price: {product.get('price', 'N/A')}")
        print(f"   Volume: {product.get('volume_weight', 'N/A')}")
        print(f"   Multipack: {product.get('multipack', 'N/A')}")
        print(f"   Slug: {product.get('slug', 'N/A')}")

if __name__ == '__main__':
    main()

