import redis from 'redis'

const client = redis.createClient();

client.on('connection', () => {
    console.log('Redis client connected to the server');
});
client.on('error', error => {
    console.log(`Redis client not connected to the server: ${error}`);
});

client.connect


function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print)
}

function displaySchoolValue(schoolName) {
    let name = client.get(schoolName);
    console.log(name);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');



