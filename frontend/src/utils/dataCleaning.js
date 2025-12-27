/**
 * JavaScript implementation of data cleaning functions
 * Mirrors the Python data_cleaning.py functionality
 */

/**
 * Standardize units: convert "Grams", "G", "g", "ml", "Milliliters" to standard format
 */
export function standardizeUnits(volumeWeight) {
  if (!volumeWeight) return "";
  
  let text = volumeWeight.trim();
  
  // Pattern to match number followed by unit
  const patterns = [
    [/(\d+)\s*(?:grams?|g)\b/gi, '$1g'],
    [/(\d+)\s*(?:milliliters?|ml)\b/gi, '$1ml'],
    [/(\d+)\s*(?:liters?|litres?|l)\b/gi, '$1l'],
    [/(\d+)\s*(?:kilograms?|kg)\b/gi, '$1kg'],
  ];
  
  patterns.forEach(([pattern, replacement]) => {
    text = text.replace(pattern, replacement);
  });
  
  return text.trim();
}

/**
 * Remove price phrases like "PMP £1.25", "PM £1", "£2.00"
 */
export function cleanPrice(price) {
  if (!price) return "";
  
  // Remove common price prefixes
  let cleaned = price.replace(/PMP\s*/gi, '');
  cleaned = cleaned.replace(/PM\s*/gi, '');
  cleaned = cleaned.replace(/RRP\s*/gi, '');
  
  // Extract price value (keep currency symbol and number)
  const priceMatch = cleaned.match(/([£$€]?\s*\d+\.?\d*)/);
  if (priceMatch) {
    return priceMatch[1].trim();
  }
  
  return cleaned.trim();
}

/**
 * Clean product name by:
 * - Standardizing casing to title case
 * - Removing unnecessary descriptors (can, bottle, bar, pack, pk)
 * - Removing extra spaces
 */
export function cleanProductName(name) {
  if (!name) return "";
  
  // Convert to title case (simple implementation)
  let cleaned = name.toLowerCase().replace(/\b\w/g, l => l.toUpperCase());
  
  // Remove unnecessary descriptors (case-insensitive)
  const descriptors = ['Can', 'Bottle', 'Bar', 'Pack', 'Pk', 'Pkt', 'Packet'];
  descriptors.forEach(descriptor => {
    const regex = new RegExp(`\\b${descriptor}\\b`, 'gi');
    cleaned = cleaned.replace(regex, '');
  });
  
  // Remove extra spaces and clean up
  cleaned = cleaned.split(/\s+/).join(' ');
  
  return cleaned.trim();
}

/**
 * Detect multipack patterns like "6x250ml", "4pk", "12 Pack"
 */
export function detectMultipack(name) {
  if (!name) return "";
  
  // Patterns for multipack detection
  const patterns = [
    /(\d+)\s*x\s*(\d+\s*(?:ml|g|l|kg))/i,  // 6x250ml
    /(\d+)\s*x\s*/i,  // 6x
    /(\d+)\s*pk\b/i,  // 4pk
    /(\d+)\s*pack\b/i,  // 12 Pack
  ];
  
  for (const pattern of patterns) {
    const match = name.match(pattern);
    if (match) {
      return match[0].trim();
    }
  }
  
  return "";
}

/**
 * Generate SEO-friendly slug from cleaned name
 */
export function generateSlug(name) {
  if (!name) return "";
  
  // Convert to lowercase
  let slug = name.toLowerCase();
  
  // Replace spaces with hyphens
  slug = slug.replace(/\s+/g, '-');
  
  // Remove special characters, keep alphanumeric and hyphens
  slug = slug.replace(/[^a-z0-9-]/g, '');
  
  // Remove multiple consecutive hyphens
  slug = slug.replace(/-+/g, '-');
  
  // Remove leading/trailing hyphens
  slug = slug.replace(/^-+|-+$/g, '');
  
  return slug;
}

