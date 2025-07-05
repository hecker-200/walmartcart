// src/components/Suggestions.jsx

import React from "react";

const Suggestions = ({ products }) => {
  if (!products || products.length === 0) {
    return <p className="text-gray-500 mt-4">No matching products found 😢</p>;
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mt-6">
      {products.map((item) => (
        <div
          key={item.id}
          className="border p-4 rounded-lg shadow hover:shadow-md transition duration-200"
        >
          <h3 className="text-lg font-semibold">{item.name}</h3>
          <p className="text-sm text-gray-600">Price: ₹{item.price}</p>
          <p className="text-sm text-gray-600">Aisle: {item.aisle}</p>
        </div>
      ))}
    </div>
  );
};

export default Suggestions;
