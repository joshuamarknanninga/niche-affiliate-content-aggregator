import { useEffect, useState } from 'react';
import ProductCard from '../components/ProductCard';
import CategoryFilter from '../components/CategoryFilter';

export default function HomePage() {
  const [products, setProducts] = useState([]);
  const [category, setCategory] = useState('all');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Get unique categories from products
  const categories = [...new Set(products.map(p => p.category))];

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const endpoint = category === 'all' 
          ? '/api/products' 
          : `/api/products/${category}`;
        
        const response = await fetch(`http://localhost:5000${endpoint}`);
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
  }, [category]);

  if (loading) return <div className="loading">Loading products...</div>;
  if (error) return <div className="error">Error: {error}</div>;

  return (
    <main>
      <h1>Best Deals in Tech & Fitness</h1>
      <CategoryFilter 
        categories={categories}
        currentCategory={category}
        setCategory={setCategory}
      />
      
      <div className="product-grid">
        {products.map(product => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </main>
  );
}