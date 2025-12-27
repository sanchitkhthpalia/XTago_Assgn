import React, { useState, useMemo } from 'react';
import { cleanProductName } from '../utils/dataCleaning';
import { detectBrand } from '../utils/brandDetection';
import './ProductTable.css';

function ProductTable() {
  const [products, setProducts] = useState([]);
  const [input, setInput] = useState('');
  const [searchTerm, setSearchTerm] = useState('');
  const [sortField, setSortField] = useState(null);
  const [sortDirection, setSortDirection] = useState('asc');

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  const handleProcess = () => {
    // Split input by newlines and filter empty lines
    const productNames = input
      .split('\n')
      .map(name => name.trim())
      .filter(name => name.length > 0);
    
    // Process each product name
    const processedProducts = productNames.map(name => ({
      originalName: name,
      cleanedName: cleanProductName(name),
      detectedBrand: detectBrand(name)
    }));
    
    setProducts(processedProducts);
  };

  const handleClear = () => {
    setInput('');
    setProducts([]);
  };

  const handleLoadSample = () => {
    const sampleData = `Coca Cola Original Taste 330ml Can
Pepsi Max 500ml Bottle
Red Bull Energy Drink 250ml Can
Lucozade Energy Original 500ml
Fanta Orange 330ml Can
Sprite Lemon Lime 330ml Can
7UP Lemon Lime 330ml Can
Tango Orange 330ml Can
Dr Pepper 330ml Can
Monster Energy 500ml Can`;
    setInput(sampleData);
  };

  // Filter and sort products
  const filteredAndSortedProducts = useMemo(() => {
    let filtered = products;
    
    // Apply search filter
    if (searchTerm) {
      const term = searchTerm.toLowerCase();
      filtered = products.filter(p => 
        p.originalName.toLowerCase().includes(term) ||
        p.cleanedName.toLowerCase().includes(term) ||
        p.detectedBrand.toLowerCase().includes(term)
      );
    }
    
    // Apply sorting
    if (sortField) {
      filtered = [...filtered].sort((a, b) => {
        const aVal = a[sortField].toLowerCase();
        const bVal = b[sortField].toLowerCase();
        const comparison = aVal.localeCompare(bVal);
        return sortDirection === 'asc' ? comparison : -comparison;
      });
    }
    
    return filtered;
  }, [products, searchTerm, sortField, sortDirection]);

  const handleSort = (field) => {
    if (sortField === field) {
      setSortDirection(sortDirection === 'asc' ? 'desc' : 'asc');
    } else {
      setSortField(field);
      setSortDirection('asc');
    }
  };

  const handleExportJSON = () => {
    const dataStr = JSON.stringify(products, null, 2);
    const dataBlob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(dataBlob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'products_cleaned.json';
    link.click();
    URL.revokeObjectURL(url);
  };

  const handleExportCSV = () => {
    const headers = ['Original Name', 'Cleaned Name', 'Detected Brand'];
    const rows = products.map(p => [
      `"${p.originalName.replace(/"/g, '""')}"`,
      `"${p.cleanedName.replace(/"/g, '""')}"`,
      `"${p.detectedBrand.replace(/"/g, '""')}"`
    ]);
    
    const csvContent = [
      headers.join(','),
      ...rows.map(row => row.join(','))
    ].join('\n');
    
    const dataBlob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(dataBlob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'products_cleaned.csv';
    link.click();
    URL.revokeObjectURL(url);
  };

  // Calculate statistics
  const stats = useMemo(() => {
    const total = products.length;
    const brands = {};
    products.forEach(p => {
      brands[p.detectedBrand] = (brands[p.detectedBrand] || 0) + 1;
    });
    const knownBrands = Object.keys(brands).filter(b => b !== 'Unknown').length;
    const unknownCount = brands['Unknown'] || 0;
    
    return {
      total,
      knownBrands,
      unknownCount,
      brandDistribution: brands
    };
  }, [products]);

  return (
    <div className="product-table-container">
      <div className="input-section">
        <h2>Paste Product Names</h2>
        <p className="instructions">
          Paste your scraped product names below (one per line), then click "Process" to see the cleaned results.
        </p>
        <div className="button-group">
          <button onClick={handleLoadSample} className="btn btn-secondary">
            Load Sample Data
          </button>
          <button onClick={handleClear} className="btn btn-secondary">
            Clear
          </button>
        </div>
        <textarea
          value={input}
          onChange={handleInputChange}
          placeholder="Paste product names here, one per line...&#10;&#10;Example:&#10;Coca Cola Original Taste 330ml Can&#10;Pepsi Max 500ml Bottle"
          className="input-textarea"
          rows="10"
        />
        <button onClick={handleProcess} className="btn btn-primary" disabled={!input.trim()}>
          Process Products
        </button>
      </div>

      {products.length > 0 && (
        <div className="results-section">
          <div className="results-header">
            <div>
              <h2>Results ({filteredAndSortedProducts.length} of {products.length} products)</h2>
              <div className="stats-bar">
                <span className="stat-item">Total: {stats.total}</span>
                <span className="stat-item">Known Brands: {stats.knownBrands}</span>
                <span className="stat-item">Unknown: {stats.unknownCount}</span>
              </div>
            </div>
            <div className="export-buttons">
              <button onClick={handleExportJSON} className="btn btn-export">
                Export JSON
              </button>
              <button onClick={handleExportCSV} className="btn btn-export">
                Export CSV
              </button>
            </div>
          </div>
          
          <div className="search-bar">
            <input
              type="text"
              placeholder="Search products..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="search-input"
            />
            {searchTerm && (
              <button onClick={() => setSearchTerm('')} className="btn-clear-search">
                Clear
              </button>
            )}
          </div>

          <div className="table-wrapper">
            <table className="product-table">
              <thead>
                <tr>
                  <th>#</th>
                  <th 
                    className="sortable"
                    onClick={() => handleSort('originalName')}
                  >
                    Original Name
                    {sortField === 'originalName' && (
                      <span className="sort-indicator">{sortDirection === 'asc' ? '↑' : '↓'}</span>
                    )}
                  </th>
                  <th 
                    className="sortable"
                    onClick={() => handleSort('cleanedName')}
                  >
                    Cleaned Name
                    {sortField === 'cleanedName' && (
                      <span className="sort-indicator">{sortDirection === 'asc' ? '↑' : '↓'}</span>
                    )}
                  </th>
                  <th 
                    className="sortable"
                    onClick={() => handleSort('detectedBrand')}
                  >
                    Detected Brand
                    {sortField === 'detectedBrand' && (
                      <span className="sort-indicator">{sortDirection === 'asc' ? '↑' : '↓'}</span>
                    )}
                  </th>
                </tr>
              </thead>
              <tbody>
                {filteredAndSortedProducts.length === 0 ? (
                  <tr>
                    <td colSpan="4" className="no-results">
                      No products match your search criteria
                    </td>
                  </tr>
                ) : (
                  filteredAndSortedProducts.map((product, index) => (
                    <tr key={index}>
                      <td className="index-cell">{index + 1}</td>
                      <td className="original-cell">{product.originalName}</td>
                      <td className="cleaned-cell">{product.cleanedName}</td>
                      <td className="brand-cell">
                        <span className={`brand-badge ${product.detectedBrand === 'Unknown' ? 'unknown' : 'known'}`}>
                          {product.detectedBrand}
                        </span>
                      </td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  );
}

export default ProductTable;

