import React from "react";
import { motion } from "framer-motion";

const ProductCard = ({ item }) => {
  return (
    <motion.div
      whileHover={{ scale: 1.05, rotateY: 5 }}
      initial={{ opacity: 0, y: 50 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4 }}
      className="border rounded-lg p-4 shadow hover:shadow-lg transition duration-200 w-full sm:w-64"
      style={{
        background: "#fff",
        borderRadius: "12px",
        boxShadow: "0 8px 20px rgba(0,0,0,0.1)",
        transformStyle: "preserve-3d",
      }}
    >
      <h3 className="text-lg font-semibold">{item.name}</h3>
      <p className="text-sm text-gray-700">Price: ₹{item.price}</p>
      <p className="text-sm text-gray-500">Aisle: {item.aisle}</p>
    </motion.div>
  );
};

export default ProductCard;
