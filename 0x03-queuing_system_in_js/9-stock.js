import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const PORT = 1245;
const DATA = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

app.use(express.json());

function getItemById(id) {
  const item = DATA.find((i) => i.id === id);
  if (!item) {
    throw new Error('Item not found');
  }
  return item;
}

app.get('/list_products', (req, res) => {
  res.json(DATA);
});

const client = createClient();

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const getAsync = promisify(client.get).bind(client);
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock) : 0;
}

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  try {
    const item = getItemById(itemId);
    const currentStock = await getCurrentReservedStockById(itemId);
    const availableStock = item.stock - currentStock;
    res.json({
      ...item,
      currentQuantity: availableStock,
    });
  } catch (error) {
    res.status(404).json({ status: 'Product not found' });
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  try {
    const item = getItemById(itemId);
    const currentStock = await getCurrentReservedStockById(itemId);
    const availableStock = item.stock - currentStock;
    if (availableStock <= 0) {
      res.status(403).json({ status: 'Not enough stock available', itemId });
      return;
    }
    reserveStockById(itemId, currentStock + 1);
    res.json({ status: 'Reservation confirmed', itemId });
  } catch (error) {
    res.status(404).json({ status: 'Product not found' });
  }
});

app.listen(PORT, () => {
  console.log(`API listening on localhost:${PORT}`);
});

export default app;
