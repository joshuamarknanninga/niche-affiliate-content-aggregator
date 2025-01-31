import React from 'react';

const ProductCard = ({ product }) => {
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
      >
        Buy Now →
      </a>
    </div>
  );
};

export default ProductCard;