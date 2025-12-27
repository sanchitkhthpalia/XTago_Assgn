"""
Unit tests for brand detection
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from brand_detection import detect_brand

def test_brand_detection():
    """Test brand detection"""
    # Known brands
    assert detect_brand("Coca Cola Original Taste") == "Coca Cola"
    assert detect_brand("Pepsi Max 500ml") == "Pepsi"
    assert detect_brand("Red Bull Energy Drink") == "Red Bull"
    assert detect_brand("Lucozade Energy") == "Lucozade"
    assert detect_brand("Fanta Orange") == "Fanta"
    assert detect_brand("Sprite Lemon") == "Sprite"
    
    # Unknown brands
    assert detect_brand("Unknown Product Name") == "Unknown"
    assert detect_brand("Generic Drink 500ml") == "Unknown"
    assert detect_brand("") == "Unknown"
    
    # Case insensitive
    assert detect_brand("coca cola") == "Coca Cola"
    assert detect_brand("PEPSI MAX") == "Pepsi"
    
    print("✅ Brand detection tests passed")

def run_all_tests():
    """Run all tests"""
    print("=" * 50)
    print("Running Brand Detection Tests")
    print("=" * 50)
    test_brand_detection()
    print("=" * 50)
    print("All tests passed! ✅")
    print("=" * 50)

if __name__ == '__main__':
    run_all_tests()

