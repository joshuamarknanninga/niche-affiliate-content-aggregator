export default function CategoryFilter({ categories, currentCategory, setCategory }) {
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
            {category.charAt(0).toUpperCase() + category.slice(1)}
          </button>
        ))}
      </div>
    );
  }