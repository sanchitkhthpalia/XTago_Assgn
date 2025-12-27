import React from 'react';
import ProductTable from './components/ProductTable';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Product Data Cleaner</h1>
        <p className="subtitle">Clean product names and detect brands from scraped data</p>
      </header>
      <main className="App-main">
        <ProductTable />
      </main>
      <footer className="App-footer">
        <p>Product Data Processing Tool - Developer Test Assignment</p>
        <p className="footer-author">
          Developed by{' '}
          <a 
            href="https://www.linkedin.com/in/sanchit-kathpalia-a841b5252/" 
            target="_blank" 
            rel="noopener noreferrer"
            className="author-link"
          >
            Sanchit Kathpalia
          </a>
        </p>
      </footer>
    </div>
  );
}

export default App;

