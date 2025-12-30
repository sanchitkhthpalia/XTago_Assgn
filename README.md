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

## Step 4: Test React UI (Without Backend - Product Processing Only)

**Note:** This tests product name processing. For live scraping, backend is required (see Step 5).

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

**Note:** To scrape websites from UI, you need backend running (Step 5)

---

## Step 5: Setup Backend API (REQUIRED for Live Scraping)

**⚠️ IMPORTANT: Backend MUST be running for scraping websites from UI**

**Terminal 1 - Start Backend:**
```bash
cd backend
pip install -r requirements.txt
python app.py
```
**Expected:** 
```
Starting Scraper API Server...
API will be available at http://localhost:5000
```

**Keep this terminal open** - Backend must stay running!

**Terminal 2 - Start Frontend:**
```bash
cd frontend
npm start
```

---

## Step 6: Test Live Scraping from UI

**Prerequisite:** Backend must be running (Step 5)

1. In browser (`http://localhost:3000`), click "Show Site Selection"
2. Select "Custom URL"
3. Enter: `http://books.toscrape.com/`
4. Set Max Products: `10`
5. Click "Scrape Products"
6. **Expected:** 
   - Button shows "Scraping..."
   - Products appear in table after 10-30 seconds
   - Shows scraped book titles, prices, etc.

**If you see an error:** Make sure backend is running on port 5000

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

### Option 1: Without Backend (Product Name Processing Only)

**No backend required** - Works offline:
1. Start frontend: `cd frontend && npm start`
2. Open `http://localhost:3000`
3. Click "Load Sample Data" or paste product names
4. Click "Process Products"
5. View results table
6. Use Search, Sort, Export features

**Note:** This mode only processes product names you paste. It does NOT scrape websites.

---

### Option 2: With Backend (Live Web Scraping)

**Backend MUST be running** for scraping websites from UI:

**Step 1: Start Backend (Terminal 1)**
```bash
cd backend
pip install -r requirements.txt
python app.py
```
**Important:** Backend must be running on `http://localhost:5000` before scraping

**Step 2: Start Frontend (Terminal 2)**
```bash
cd frontend
npm start
```

**Step 3: Scrape from UI**
1. Open `http://localhost:3000`
2. Click "Show Site Selection"
3. Select site or enter custom URL (e.g., `http://books.toscrape.com/`)
4. Set Max Products
5. Click "Scrape Products"
6. Wait for results (10-30 seconds)
7. View scraped results in table

**Features Available:**
- ✅ Live web scraping from any URL
- ✅ Search/Filter products
- ✅ Sort by columns
- ✅ Export to JSON/CSV
- ✅ View statistics

**If Backend Not Running:**
- ❌ "Scrape Products" button will show error
- ✅ "Process Products" (paste names) still works

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
- The React UI has two modes:
  - **Product Name Processing:** Works without backend (client-side)
  - **Live Web Scraping:** Requires backend API running on port 5000
- All data cleaning logic is implemented in both Python and JavaScript

## Deploy Backend API

### Option 1: Deploy to Render (Recommended - Free)

**Step 1: Create Account**
- Go to https://render.com
- Sign up with GitHub

**Step 2: Create New Web Service**
1. Click "New +" → "Web Service"
2. Connect your GitHub repository: `sanchitkhthpalia/XTago_Assgn`
3. Configure:
   - **Name:** `product-scraper-api`
   - **Root Directory:** `backend`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
4. Click "Create Web Service"

**Step 3: Get Backend URL**
- After deployment, you'll get a URL like: `https://product-scraper-api.onrender.com`
- Copy this URL

**Step 4: Update Frontend**
- In Vercel/Netlify, add environment variable:
  - `REACT_APP_API_URL=https://product-scraper-api.onrender.com`
- Redeploy frontend

---

### Option 2: Deploy to Railway (Free Tier)

**Step 1: Create Account**
- Go to https://railway.app
- Sign up with GitHub

**Step 2: Deploy**
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose your repository
4. Railway auto-detects Python
5. Set **Root Directory:** `backend`
6. Railway will auto-deploy

**Step 3: Get URL**
- Railway provides URL: `https://your-app.railway.app`
- Copy this URL

**Step 4: Update Frontend**
- Set `REACT_APP_API_URL` to Railway URL

---

### Option 3: Deploy to Heroku

**Step 1: Install Heroku CLI**
```bash
# Download from https://devcenter.heroku.com/articles/heroku-cli
```

**Step 2: Login**
```bash
heroku login
```

**Step 3: Create App**
```bash
cd backend
heroku create your-app-name
```

**Step 4: Deploy**
```bash
git init
git add .
git commit -m "Initial commit"
git push heroku main
```

**Step 5: Get URL**
- Heroku provides: `https://your-app-name.herokuapp.com`

---

### Quick Deploy Commands (Render)

```bash
# 1. Push code to GitHub (already done)
# 2. Go to render.com
# 3. Connect repo
# 4. Set Root Directory: backend
# 5. Set Start Command: gunicorn app:app --bind 0.0.0.0:$PORT
# 6. Deploy!
```

**✅ Backend URL:** `https://product-scraper-api-9gf9.onrender.com`

---

### After Backend Deployment

**✅ Backend is deployed at:** `https://product-scraper-api-9gf9.onrender.com`

1. **Update frontend environment variable:**
   - **For Local Development:** Create `frontend/.env` file:
     ```
     REACT_APP_API_URL=https://product-scraper-api-9gf9.onrender.com
     ```
   - **For Production (Vercel/Netlify):** 
     - Go to Project Settings → Environment Variables
     - Add: `REACT_APP_API_URL=https://product-scraper-api-9gf9.onrender.com`
2. **Redeploy frontend** (or restart local dev server)
3. **Test:** Scraping should now work from deployed frontend!

**Test Backend:**
- Health Check: https://product-scraper-api-9gf9.onrender.com/api/health
- List Sites: https://product-scraper-api-9gf9.onrender.com/api/sites

---

## License

This project is created for a developer test assignment.

## Author

**Developed by [Sanchit Kathpalia](https://www.linkedin.com/in/sanchit-kathpalia-a841b5252/)**

Product Data Processing Tool - Developer Test Assignment

