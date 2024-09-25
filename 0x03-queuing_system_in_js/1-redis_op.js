import {createClient, print} from 'redis'

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', error => {
    console.log(`Redis client not connected to the server: ${error}`);
});



function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print)
}

function displaySchoolValue(schoolName) {
    let name = client.get(schoolName, (err, reply) => {
        console.log(reply)
    });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');



