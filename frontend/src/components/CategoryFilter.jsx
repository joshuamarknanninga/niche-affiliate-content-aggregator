// src/components/CategoryFilter.jsx
import React from 'react';

const CategoryFilter = ({ categories, currentCategory, setCategory }) => {
  return (
    <div className="category-filter">
      <button 
        onClick={() => setCategory('all')}
        className={currentCategory === 'all' ? 'active' : ''}
      >
        All
      </button>
      {categories.map(category => (
        <button
          key={category}
          onClick={() => setCategory(category)}
          className={currentCategory === category ? 'active' : ''}
        >
          {category}
        </button>
      ))}
    </div>
  );
};

export default CategoryFilter;