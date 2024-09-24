import { createClient, print } from 'redis';

const client = createClient();

const KEY = 'HolbertonSchools';

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.hset(KEY, 'Portland', 50, print);
client.hset(KEY, 'Seattle', 80, print);
client.hset(KEY, 'New York', 20, print);
client.hset(KEY, 'Bogota', 20, print);
client.hset(KEY, 'Cali', 40, print);
client.hset(KEY, 'Paris', 2, print);

client.hgetall(KEY, (err, result) => {
  if (err) {
    console.error('Error retrieving hash:', err);
  } else {
    console.log(result);
  }
});
