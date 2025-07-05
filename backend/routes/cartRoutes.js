import express from 'express';
import { generateCart } from '../controllers/cartController.js';

const router = express.Router();

router.post('/generate', generateCart);

export default router;
