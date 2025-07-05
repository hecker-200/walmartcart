import React, { useState } from 'react';
import { motion } from 'framer-motion';

function GoalInput({ onSubmit }) {
  const [goal, setGoal] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (goal.trim()) onSubmit(goal);
  };

  return (
    <motion.form
      initial={{ x: -100, opacity: 0 }}
      animate={{ x: 0, opacity: 1 }}
      transition={{ type: 'spring', stiffness: 60 }}
      onSubmit={handleSubmit}
      style={{ marginBottom: '1rem' }}
    >
      <input
        type="text"
        placeholder="e.g. snacks under ₹300"
        value={goal}
        onChange={(e) => setGoal(e.target.value)}
        style={{ padding: '10px', width: '300px' }}
      />
      <button
        type="submit"
        style={{
          marginLeft: '10px',
          padding: '10px',
          background: '#4f46e5',
          color: '#fff',
          border: 'none',
          borderRadius: '4px',
        }}
      >
        Get Suggestions
      </button>
    </motion.form>
  );
}

export default GoalInput;
