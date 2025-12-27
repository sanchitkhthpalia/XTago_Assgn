"""
Data validation and quality metrics
"""
import json
import os
from typing import Dict, List, Any

def validate_product(product: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate a single product and return validation results
    """
    issues = []
    warnings = []
    
    # Required fields
    required_fields = ['name', 'price', 'volume_weight']
    for field in required_fields:
        if not product.get(field):
            issues.append(f"Missing required field: {field}")
    
    # Name validation
    name = product.get('name', '')
    if name:
        if len(name) < 3:
            warnings.append("Product name is very short")
        if len(name) > 200:
            warnings.append("Product name is very long")
    
    # Price validation
    price = product.get('price', '')
    if price:
        import re
        if not re.search(r'[£$€]\s*\d+', price):
            warnings.append("Price format may be incorrect")
    
    # Volume/Weight validation
    volume_weight = product.get('volume_weight', '')
    if volume_weight:
        import re
        if not re.search(r'\d+\s*(ml|g|l|kg)', volume_weight, re.I):
            warnings.append("Volume/weight format may be incorrect")
    
    # Brand validation
    brand = product.get('brand', '')
    if brand == 'Unknown':
        warnings.append("Brand not detected")
    
    return {
        'valid': len(issues) == 0,
        'issues': issues,
        'warnings': warnings,
        'completeness_score': calculate_completeness(product)
    }

def calculate_completeness(product: Dict[str, Any]) -> float:
    """
    Calculate completeness score (0-1) for a product
    """
    fields = ['name', 'price', 'volume_weight', 'image_url', 'brand', 'slug']
    present_fields = sum(1 for field in fields if product.get(field))
    return present_fields / len(fields)

def validate_products(products: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Validate a list of products and return quality metrics
    """
    validation_results = [validate_product(p) for p in products]
    
    total = len(products)
    valid_count = sum(1 for r in validation_results if r['valid'])
    invalid_count = total - valid_count
    
    avg_completeness = sum(r['completeness_score'] for r in validation_results) / total if total > 0 else 0
    
    total_issues = sum(len(r['issues']) for r in validation_results)
    total_warnings = sum(len(r['warnings']) for r in validation_results)
    
    # Brand distribution
    brands = {}
    for product in products:
        brand = product.get('brand', 'Unknown')
        brands[brand] = brands.get(brand, 0) + 1
    
    unknown_brand_count = brands.get('Unknown', 0)
    known_brand_percentage = ((total - unknown_brand_count) / total * 100) if total > 0 else 0
    
    return {
        'total_products': total,
        'valid_products': valid_count,
        'invalid_products': invalid_count,
        'validity_percentage': (valid_count / total * 100) if total > 0 else 0,
        'average_completeness': round(avg_completeness * 100, 2),
        'total_issues': total_issues,
        'total_warnings': total_warnings,
        'brand_distribution': brands,
        'known_brand_percentage': round(known_brand_percentage, 2),
        'unknown_brand_count': unknown_brand_count,
        'validation_results': validation_results
    }

def print_quality_report(metrics: Dict[str, Any]):
    """
    Print a quality report
    """
    print("\n" + "=" * 60)
    print("Data Quality Report")
    print("=" * 60)
    print(f"Total Products: {metrics['total_products']}")
    print(f"Valid Products: {metrics['valid_products']} ({metrics['validity_percentage']:.1f}%)")
    print(f"Invalid Products: {metrics['invalid_products']}")
    print(f"Average Completeness: {metrics['average_completeness']}%")
    print(f"Total Issues: {metrics['total_issues']}")
    print(f"Total Warnings: {metrics['total_warnings']}")
    print(f"\nBrand Detection:")
    print(f"  Known Brands: {metrics['known_brand_percentage']:.1f}%")
    print(f"  Unknown Brands: {metrics['unknown_brand_count']}")
    print(f"\nTop Brands:")
    sorted_brands = sorted(metrics['brand_distribution'].items(), key=lambda x: x[1], reverse=True)
    for brand, count in sorted_brands[:10]:
        print(f"  {brand}: {count}")
    print("=" * 60)

def main():
    """Test validation on sample data"""
    input_file = '../data/products_final.json'
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return
    
    with open(input_file, 'r', encoding='utf-8') as f:
        products = json.load(f)
    
    metrics = validate_products(products)
    print_quality_report(metrics)

if __name__ == '__main__':
    main()

