// src/pages/HomePage.jsx
import { useEffect, useState } from 'react';
import ProductList from '../components/ProductList';

const HomePage = ({ selectedCategory }) => {
  // Move ALL useState hooks INSIDE the component
  const [searchTerm, setSearchTerm] = useState(''); // <-- Fix here
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        // Also fix port to 5000 (matches backend)
        const response = await fetch('http://localhost:5001/api/products');
        if (!response.ok) throw new Error('Failed to fetch');
        const data = await response.json();
        setProducts(data.products);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, [selectedCategory]);

  if (loading) return <div className="loading">Loading products...</div>;
  if (error) return <div className="error">Error: {error}</div>;

  return <ProductList products={products} />;
};

export default HomePage;