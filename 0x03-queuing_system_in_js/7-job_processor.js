import { createQueue } from 'kue';
import fs from 'fs';


const jobs = JSON.parse(fs.readFileSync('jobs.json', 'utf-8'));

const queue = createQueue({ name: 'push_notification_code_2' });

for (const jobInfo of jobs) {
    const job = queue.create('push_notification_code_2', jobInfo);

    job
        .on('enqueue', () => {
            console.log('Notification job created:', job.id);
        })
        .on('complete', () => {
            console.log('Notification job', job.id, 'completed');
        })
        .on('failed', (err) => {
            console.log('Notification job', job.id, 'failed:', err.message || err.toString());
        })
        .on('progress', (progress, _data) => {
            console.log('Notification job', job.id, `${progress}% complete`);
        });
    job.save();
}