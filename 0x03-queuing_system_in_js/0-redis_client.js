import {createClient} from 'redis'

const client = createClient();

client.on('connection', () => {
    console.log('Redis client connected to the server');
});
client.on('error', error => {
    console.log(`Redis client not connected to the server: ${error}`);
});

client.connect().catch((err) => {
    console.error('Error connecting to Redis:', err);
});

