// src/App.jsx
import { useState } from 'react';
import HomePage from "./pages/HomePage";
import CategoryFilter from "./components/CategoryFilter.jsx";
import ProductList from "./components/ProductList.jsx";
import "./App.css";

function App() {
  const [selectedCategory, setSelectedCategory] = useState('all');
  const categories = ['programming', 'fitness', 'books']; // Add your actual categories

  return (
    <div className="app">
      <h1>Affiliate Product Aggregator</h1>
      <CategoryFilter
        categories={categories}
        activeCategory={selectedCategory}
        setCategory={setSelectedCategory}
      />
      <HomePage selectedCategory={selectedCategory} />
    </div>
  );
}

export default App;