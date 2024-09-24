import express from 'express';
import { createQueue } from 'kue';
import { createClient } from 'redis';
import { promisify } from 'util';

const AVAILABLE_SEATS = 50;
let reservationEnabled = true;

const app = express();
const queue = createQueue();
const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

const reserveSeatAsync = promisify(client.set).bind(client);
const getCurrentAvailableSeatsAsync = promisify(client.get).bind(client);

async function initializeAvailableSeats() {
  await reserveSeatAsync('available_seats', AVAILABLE_SEATS);
}
// Initialize seats on server start
initializeAvailableSeats();

async function reserveSeat(number) {
  await reserveSeatAsync('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const seats = await getCurrentAvailableSeatsAsync('available_seats');
  return seats ? parseInt(seats, 10) : 0;
}

app.use(express.json());

// GET /available_seats
app.get('/available_seats', async (req, res) => {
  try {
    const seats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats: seats });
  } catch (error) {
    res.json({ status: `Failed to retrieve available seats: ${error.message}` });
  }
});

// GET /reserve_seat
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat', {}).save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err}`);
  });
});

// GET /process
app.get('/process', (req, res) => {
  if (!reservationEnabled)
    return res.json({ status: 'Queue is disabled. No more jobs!' });
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    try {
      const availableSeats = await getCurrentAvailableSeats();
      const newAvailableSeats = availableSeats - 1;

      if (newAvailableSeats === 0) reservationEnabled = false;
      if (newAvailableSeats < 0) return done(new Error('Not enough seats available'));
      await reserveSeat(newAvailableSeats);
      return done();
    } catch (error) {
      return done(error);
    }
  });
});

const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

export default app;
