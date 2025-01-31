import { useState } from 'react';

export default function ProductCard({ product }) {
  const [isTracking, setIsTracking] = useState(false);

  const trackClick = async () => {
    if (isTracking) return; // Prevent duplicate tracking
    
    try {
      setIsTracking(true);
      const response = await fetch(`http://localhost:5000/api/track/${product.id}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          userAgent: navigator.userAgent,
          timestamp: new Date().toISOString(),
        }),
      });

      if (!response.ok) {
        throw new Error('Tracking failed');
      }
      
      console.log('Click tracked successfully');
    } catch (error) {
      console.error('Tracking error:', error);
    } finally {
      setIsTracking(false);
    }
  };

  return (
    <div className="product-card">
      <h3>{product.title}</h3>
      <p className="price">{product.price}</p>
      <p className="description">{product.description}</p>
      <a 
        href={product.url} 
        target="_blank" 
        rel="noopener noreferrer"
        className="affiliate-link"
        onClick={trackClick}
      >
        {isTracking ? 'Redirecting...' : 'Buy Now →'}
      </a>
    </div>
  );
}