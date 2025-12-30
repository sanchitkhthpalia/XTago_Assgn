/**
 * Available scraping sites configuration
 * Mirrors the Python config.py
 */

export const SCRAPING_SITES = {
  wegetanystock: {
    name: 'We Get Any Stock',
    baseUrl: 'https://www.wegetanystock.com/',
    enabled: true,
    description: 'Default site for product scraping'
  },
  custom: {
    name: 'Custom URL',
    baseUrl: '',
    enabled: true,
    description: 'Enter your own website URL'
  }
};

export const getAvailableSites = () => {
  return Object.entries(SCRAPING_SITES)
    .filter(([key, site]) => site.enabled)
    .map(([key, site]) => ({ key, ...site }));
};

export const getSiteByKey = (key) => {
  return SCRAPING_SITES[key] || null;
};

