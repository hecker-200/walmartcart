import express from 'express';
import cors from 'cors';
import cartRoutes from './routes/cartRoutes.js';
import dotenv from 'dotenv';
dotenv.config();

const app = express();
const PORT = 3001;

app.use(cors());
app.use(express.json());

// Mount all routes
app.use('/api/cart', cartRoutes);

app.listen(PORT, () => {
  console.log(`🚀 Node server running on http://localhost:${PORT}`);
});
