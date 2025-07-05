import React from 'react';
import { motion } from 'framer-motion';

function CartSummary({ items }) {
  const total = items.reduce((sum, item) => sum + item.price, 0);

  return (
    <motion.div
      initial={{ scale: 0.5, opacity: 0 }}
      animate={{ scale: 1, opacity: 1 }}
      transition={{ type: 'spring', bounce: 0.4, duration: 0.8 }}
      style={{ marginTop: '2rem', padding: '1rem', background: '#fefce8', borderRadius: '12px' }}
    >
      <h2>Total: ₹{total}</h2>
      <p>🧠 Don’t forget to check for essentials like tissues, bags, etc!</p>
    </motion.div>
  );
}

export default CartSummary;
