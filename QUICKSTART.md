# Quick Start Guide

## Quick Setup (5 minutes)

### 1. Setup Python Environment

```bash
cd scraper
pip install -r requirements.txt
```

### 2. Run the Scraper

```bash
python process_data.py
```

This will:
- Scrape products from wegetanystock.com
- Clean the data
- Detect brands
- Save to `../data/products_final.json`

### 3. Setup React Frontend

Open a new terminal:

```bash
cd frontend
npm install
npm start
```

The React app will open at `http://localhost:3000/`

## Testing Individual Components

### Test Data Cleaning
```bash
cd scraper
python data_cleaning.py
```

### Test Brand Detection
```bash
cd scraper
python brand_detection.py
```

### Test Scraper Only
```bash
cd scraper
python scraper.py
```

## Using the React UI

1. Open `http://localhost:3000/` in your browser
2. Click "Load Sample Data" to see example products
3. Or paste your own product names (one per line)
4. Click "Process Products"
5. View the results table

## Sample Product Names to Test

Copy and paste these into the React UI:

```
Coca Cola Original Taste 330ml Can
Pepsi Max 500ml Bottle
Red Bull Energy Drink 250ml Can
Lucozade Energy Original 500ml
Fanta Orange 330ml Can
Sprite Lemon Lime 330ml Can
7UP Lemon Lime 330ml Can
Tango Orange 330ml Can
Dr Pepper 330ml Can
Monster Energy 500ml Can
```

## Expected Output

After processing, you should see:
- **Cleaned Names**: Title case, descriptors removed
- **Detected Brands**: Brand names or "Unknown"
- **Formatted Data**: Ready for use in your application

## Troubleshooting

**Python errors?**
- Make sure you're in the `scraper` directory
- Check Python version: `python --version` (should be 3.7+)
- Reinstall dependencies: `pip install -r requirements.txt --upgrade`

**React errors?**
- Make sure you're in the `frontend` directory
- Delete `node_modules` and reinstall: `rm -rf node_modules && npm install`
- Clear npm cache: `npm cache clean --force`

**Scraper not finding products?**
- The scraper includes fallback sample data
- Check your internet connection
- The website structure may have changed

