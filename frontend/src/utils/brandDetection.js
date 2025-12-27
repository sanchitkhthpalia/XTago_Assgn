/**
 * JavaScript implementation of brand detection
 * Mirrors the Python brand_detection.py functionality
 */

// Hardcoded brand list
const BRANDS = [
  "Coca-Cola", "Coca Cola", "Coke",
  "Lucozade",
  "Red Bull",
  "Pepsi",
  "Fanta",
  "Sprite",
  "7UP", "7-Up",
  "Tango",
  "Dr Pepper", "Dr. Pepper",
  "Monster",
  "Rockstar",
  "Relentless",
  "Powerade",
  "Gatorade",
  "Ribena",
  "Robinsons",
  "Innocent",
  "Tropicana",
  "Ocean Spray",
  "Volvic",
  "Evian",
  "Highland Spring",
];

/**
 * Detect brand from product name
 * Returns brand name if found, "Unknown" otherwise
 */
export function detectBrand(name) {
  if (!name) return "Unknown";
  
  const nameLower = name.toLowerCase();
  
  // Check each brand (case-insensitive)
  for (const brand of BRANDS) {
    const brandLower = brand.toLowerCase();
    
    // Exact match or brand appears in name
    if (nameLower.includes(brandLower)) {
      // Return the original brand name (with proper casing)
      return brand;
    }
  }
  
  return "Unknown";
}

