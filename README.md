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

## How to Test Everything - Complete Step-by-Step Guide

### Prerequisites Check
```bash
python --version  # Need 3.7+
node --version    # Need 14+
```

---

## Step 1: Setup Python Environment

```bash
cd scraper
pip install -r requirements.txt
```

---

## Step 2: Test Python Scraper

### 2.1: List Available Sites
```bash
python process_data.py --list-sites
```
**Expected:** Shows list of available sites

### 2.2: Scrape from Books to Scrape (Best Test Site)
```bash
python process_data.py --site custom --url http://books.toscrape.com/ --max 10
```
**Expected:** Scrapes 10 products, cleans data, detects brands, saves to `data/products_final.json`

### 2.3: Test Data Cleaning
```bash
python data_cleaning.py
```
**Expected:** Shows sample cleaned products

### 2.4: Test Brand Detection
```bash
python brand_detection.py
```
**Expected:** Shows brand detection test results

### 2.5: Run Unit Tests
```bash
python tests/test_data_cleaning.py
python tests/test_brand_detection.py
```
**Expected:** All tests pass ✅

---

## Step 3: Setup React Frontend

```bash
cd frontend
npm install
```

---

## Step 4: Test React UI (Without Backend)

```bash
cd frontend
npm start
```
**Opens:** `http://localhost:3000`

### Test 4.1: Process Product Names
1. Click "Load Sample Data"
2. Click "Process Products"
3. **Expected:** Table shows 10 products

### Test 4.2: Search/Filter
1. Type "Coca" in search box
2. **Expected:** Filters to Coca Cola products

### Test 4.3: Sort
1. Click "Detected Brand" header
2. **Expected:** Products sort by brand

### Test 4.4: Export
1. Click "Export JSON" or "Export CSV"
2. **Expected:** File downloads

---

## Step 5: Setup Backend API (For Live Scraping)

**Terminal 1:**
```bash
cd backend
pip install -r requirements.txt
python app.py
```
**Expected:** Server starts on `http://localhost:5000`

**Terminal 2 (keep frontend running):**
```bash
cd frontend
npm start
```

---

## Step 6: Test Live Scraping from UI

1. In browser, click "Show Site Selection"
2. Select "Custom URL"
3. Enter: `http://books.toscrape.com/`
4. Set Max Products: `10`
5. Click "Scrape Products"
6. **Expected:** Products appear in table after 10-30 seconds

---

## Step 7: Complete Workflow Test

1. Scrape 20 products from Books to Scrape via UI
2. Search/Filter products
3. Sort by brand
4. Export to JSON
5. Verify exported file has 20 products

---

## Quick Test Commands

```bash
# Test scraper
cd scraper && python process_data.py --site custom --url http://books.toscrape.com/ --max 5

# Test cleaning
python data_cleaning.py

# Test brand detection  
python brand_detection.py

# Start backend (Terminal 1)
cd backend && python app.py

# Start frontend (Terminal 2)
cd frontend && npm start
```

---

## How to Run the Scraper

### Option A: Interactive Menu
```bash
cd scraper
python scrape_site.py
```

### Option B: Command Line
```bash
# Default site
python process_data.py

# Specific site
python process_data.py --site wegetanystock

# Custom URL
python process_data.py --site custom --url http://books.toscrape.com/

# With max products
python process_data.py --site custom --url http://books.toscrape.com/ --max 50

# List sites
python process_data.py --list-sites
```

---

## How to Test the Cleaning Script

```bash
cd scraper
python data_cleaning.py        # Test cleaning functions
python brand_detection.py      # Test brand detection
python tests/test_data_cleaning.py    # Run unit tests
python tests/test_brand_detection.py  # Run unit tests
```

---

## How to Use the React UI

### Without Backend (Product Name Processing):
1. Open `http://localhost:3000`
2. Click "Load Sample Data" or paste product names
3. Click "Process Products"
4. View results table
5. Use Search, Sort, Export features

### With Backend (Live Scraping):
1. Start backend: `cd backend && python app.py`
2. Start frontend: `cd frontend && npm start`
3. Click "Show Site Selection"
4. Select site or enter custom URL
5. Click "Scrape Products"
6. View scraped results

**Features:**
- Search/Filter products
- Sort by columns
- Export to JSON/CSV
- View statistics

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

