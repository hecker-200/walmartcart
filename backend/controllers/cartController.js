import axios from 'axios';
import dotenv from 'dotenv';
dotenv.config();

export const generateCart = async (req, res) => {
  try {
    const response = await axios.post(process.env.ML_API_URL, req.body);
    res.json(response.data);
  } catch (error) {
    console.error("❌ ML connection failed:", error.message);
    res.status(500).json({ error: "ML service not responding 😢" });
  }
};
