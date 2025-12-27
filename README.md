# Product Data Scraper and Cleaner

A complete project for scraping product data from wegetanystock.com, cleaning the data, detecting brands, and providing a React UI for preview and testing.

## Project Structure

```
XRapido_Assgn/
├── scraper/                 # Python scraping and data processing
│   ├── scraper.py          # Web scraper for wegetanystock.com
│   ├── data_cleaning.py    # Data cleaning functions
│   ├── brand_detection.py  # Brand detection logic
│   ├── process_data.py     # Main processing pipeline
│   ├── requirements.txt    # Python dependencies
│   └── __init__.py
├── frontend/               # React UI application
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── ProductTable.js
│   │   │   └── ProductTable.css
│   │   ├── utils/
│   │   │   ├── dataCleaning.js
│   │   │   └── brandDetection.js
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   └── index.css
│   └── package.json
├── data/                   # Output directory for scraped data
│   ├── products_raw.json      # Raw scraped data
│   ├── products_cleaned.json  # Cleaned data
│   └── products_final.json    # Final data with brands
└── README.md

```

## Features

### 1. Web Scraping
- Scrapes product data from wegetanystock.com
- Extracts: Product Name, Price, Volume/Weight, Image URL
- Handles pagination and multiple categories
- Falls back to sample data if scraping is limited
- Configurable settings via `config.py`

### 2. Data Cleaning
- **Unit Standardization**: Converts "Grams", "G", "g", "ml", "Milliliters" to standard format (e.g., "500g", "330ml")
- **Price Cleaning**: Removes price phrases like "PMP £1.25", "PM £1", "£2.00"
- **Casing Standardization**: Converts product names to title case (e.g., "coca cola" → "Coca Cola")
- **Descriptor Removal**: Removes unnecessary words like "can", "bottle", "bar", "pack", "pk"

### 3. Brand Detection
- Detects brands from a hardcoded list including:
  - Coca-Cola, Pepsi, Red Bull, Lucozade, Fanta, Sprite, 7UP, Tango, Dr Pepper, Monster, and more
- Returns "Unknown" if no brand is detected
- Configurable brand list in `config.py`

### 4. Bonus Features
- **Multipack Detection**: Detects patterns like "6x250ml", "4pk", "12 Pack"
- **SEO-Friendly Slugs**: Generates slugs like "coca-cola-zero-330ml" from product names
- **JSON Output**: Saves cleaned results to JSON files
- **Data Validation**: Quality metrics and validation reports
- **Unit Tests**: Comprehensive test suite for all functions

### 5. React UI (Enhanced)
- Clean, modern interface for testing data cleaning
- Paste product names and preview results
- Shows Original Name, Cleaned Name, and Detected Brand
- **NEW: Search/Filter** - Filter products by name or brand
- **NEW: Sortable Columns** - Click headers to sort
- **NEW: Export Functionality** - Export to JSON or CSV
- **NEW: Statistics Dashboard** - View data quality metrics
- Includes sample data for quick testing

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- Node.js 14 or higher
- npm or yarn

### Python Environment Setup

1. Navigate to the scraper directory:
   ```bash
   cd scraper
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Or if using a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

### React Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install npm dependencies:
   ```bash
   npm install
   ```

## How to Run

### 1. Run the Scraper

From the `scraper` directory:

```bash
python scraper.py
```

This will:
- Scrape products from wegetanystock.com
- Save raw data to `../data/products_raw.json`

**Alternative: Run the complete pipeline:**

```bash
python process_data.py
```

This will:
- Scrape products
- Clean the data
- Detect brands
- Save final output to `../data/products_final.json`

### 2. Test the Cleaning Script

You can test individual cleaning functions:

```bash
# Test data cleaning
python data_cleaning.py

# Test brand detection
python brand_detection.py

# Run unit tests
python tests/test_data_cleaning.py
python tests/test_brand_detection.py

# Or use pytest
pytest tests/
```

### 2.5. Validate Data Quality

Check the quality of your scraped and cleaned data:

```bash
python data_validation.py
```

This will show:
- Validity percentage
- Completeness scores
- Brand detection statistics
- Data quality metrics

### 3. Run the React UI

From the `frontend` directory:

```bash
npm start
```

The app will open in your browser at `http://localhost:3000/`

**Using the UI:**
1. Click "Load Sample Data" to see example products
2. Or paste your own product names (one per line)
3. Click "Process Products" to see cleaned results
4. View the table showing Original Name, Cleaned Name, and Detected Brand

**New Features:**
- **Search/Filter**: Use the search bar to filter products by name or brand
- **Sort**: Click column headers to sort by Original Name, Cleaned Name, or Brand
- **Export**: Export cleaned data to JSON or CSV format
- **Statistics**: View data quality statistics (total products, known brands, etc.)

## Data Files

The scraper generates three JSON files in the `data/` directory:

1. **products_raw.json**: Raw scraped data from the website
2. **products_cleaned.json**: Data after cleaning (name, price, volume standardization)
3. **products_final.json**: Final data including brand detection

### Sample Product Structure

```json
{
  "original_name": "Coca Cola Original Taste 330ml Can",
  "name": "Coca Cola Original Taste 330ml",
  "price": "£0.75",
  "volume_weight": "330ml",
  "image_url": "https://...",
  "multipack": "",
  "slug": "coca-cola-original-taste-330ml",
  "brand": "Coca-Cola"
}
```

## Functions Reference

### Python Functions

#### `clean_product_name(name)`
Cleans product names by standardizing casing and removing descriptors.

#### `detect_brand(name)`
Detects brand from product name using hardcoded brand list.

#### `standardize_units(volume_weight)`
Standardizes volume/weight units to consistent format.

#### `clean_price(price)`
Removes price prefixes and extracts clean price value.

#### `detect_multipack(name)`
Detects multipack patterns in product names.

#### `generate_slug(name)`
Generates SEO-friendly URL slugs from product names.

### JavaScript Functions (React UI)

The React UI includes JavaScript implementations of the same functions:
- `cleanProductName(name)`
- `detectBrand(name)`
- `standardizeUnits(volumeWeight)`
- `cleanPrice(price)`
- `detectMultipack(name)`
- `generateSlug(name)`

## Troubleshooting

### Scraper Issues
- If scraping fails, the script will generate sample data to meet requirements
- Check your internet connection
- The website structure may have changed - adjust selectors in `scraper.py` if needed

### React UI Issues
- Make sure all dependencies are installed: `npm install`
- Clear browser cache if UI doesn't update
- Check browser console for errors

### Python Import Errors
- Make sure you're running scripts from the `scraper` directory
- Verify all dependencies are installed: `pip install -r requirements.txt`

## Notes

- The scraper includes fallback mechanisms to ensure at least 50-100 products are available
- Brand detection is case-insensitive
- The React UI processes data client-side (no backend required)
- All data cleaning logic is implemented in both Python and JavaScript

## License

This project is created for a developer test assignment.

## Author

**Developed by [Sanchit Kathpalia](https://www.linkedin.com/in/sanchit-kathpalia-a841b5252/)**

Product Data Processing Tool - Developer Test Assignment

