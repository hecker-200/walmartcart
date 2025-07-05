// src/pages/Home.jsx

import React, { useState } from 'react';
import GoalInput from '../components/GoalInput';
import ProductCard from '../components/ProductCard';
import CartSummary from '../components/CartSummary';
import { getSuggestions } from '../api/mlService';

function Home() {
  const [products, setProducts] = useState([]);
  const [trending, setTrending] = useState([]);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleGoalSubmit = async (goalText) => {
    setLoading(true);
    const result = await getSuggestions(goalText);

    if (result?.products?.length > 0) {
      console.log("🛒 Products received:", result.products);
      setProducts(result.products);
      setTrending(result.products.slice(0, 3)); // simple trending logic for now
      setError('');
    } else {
      setProducts([]);
      setTrending([]);
      setError(result?.error || 'No matching products found 😢');
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>🛒 SmartCart Companion</h1>
      <GoalInput onSubmit={handleGoalSubmit} />

      {loading && <p>⏳ Loading smart suggestions...</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}

      {products.length > 0 ? (
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: '1rem' }}>
          {products.map((item, i) => (
            <ProductCard key={i} item={item} />
          ))}
        </div>
      ) : (
        !loading && <p style={{ color: 'gray' }}>No items to show</p>
      )}

      {products.length > 0 && <CartSummary items={products} />}

      {/* 🔥 Trending section always shown */}
      <h2 style={{ marginTop: '2rem' }}>🔥 Trending in Store</h2>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '1rem' }}>
        {trending.length > 0 ? (
          trending.map((item, i) => (
            <ProductCard key={`trending-${i}`} item={item} />
          ))
        ) : (
          <p style={{ color: 'gray' }}>No trending items right now.</p>
        )}
      </div>
    </div>
  );
}

export default Home;
