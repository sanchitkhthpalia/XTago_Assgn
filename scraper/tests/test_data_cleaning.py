"""
Unit tests for data cleaning functions
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_cleaning import (
    clean_product_name,
    standardize_units,
    clean_price,
    detect_multipack,
    generate_slug
)

def test_clean_product_name():
    """Test product name cleaning"""
    assert clean_product_name("coca cola 330ml can") == "Coca Cola 330Ml"
    assert clean_product_name("Pepsi Max 500ml Bottle") == "Pepsi Max 500Ml"
    assert clean_product_name("red bull energy drink") == "Red Bull Energy Drink"
    assert clean_product_name("") == ""
    print("✅ clean_product_name tests passed")

def test_standardize_units():
    """Test unit standardization"""
    assert standardize_units("500 Grams") == "500g"
    assert standardize_units("330 ml") == "330ml"
    assert standardize_units("1.5 Liters") == "1.5l"
    assert standardize_units("2 Kilograms") == "2kg"
    assert standardize_units("") == ""
    print("✅ standardize_units tests passed")

def test_clean_price():
    """Test price cleaning"""
    assert clean_price("PMP £1.25") == "£1.25"
    assert clean_price("PM £1") == "£1"
    assert clean_price("£2.00") == "£2.00"
    assert clean_price("RRP £5.99") == "£5.99"
    assert clean_price("") == ""
    print("✅ clean_price tests passed")

def test_detect_multipack():
    """Test multipack detection"""
    assert detect_multipack("Coca Cola 6x250ml") != ""
    assert detect_multipack("Pepsi 4pk") != ""
    assert detect_multipack("Red Bull 12 Pack") != ""
    assert detect_multipack("Single Product") == ""
    assert detect_multipack("") == ""
    print("✅ detect_multipack tests passed")

def test_generate_slug():
    """Test slug generation"""
    assert generate_slug("Coca Cola Zero 330ml") == "coca-cola-zero-330ml"
    assert generate_slug("Pepsi Max") == "pepsi-max"
    assert generate_slug("") == ""
    print("✅ generate_slug tests passed")

def run_all_tests():
    """Run all tests"""
    print("=" * 50)
    print("Running Data Cleaning Tests")
    print("=" * 50)
    test_clean_product_name()
    test_standardize_units()
    test_clean_price()
    test_detect_multipack()
    test_generate_slug()
    print("=" * 50)
    print("All tests passed! ✅")
    print("=" * 50)

if __name__ == '__main__':
    run_all_tests()

