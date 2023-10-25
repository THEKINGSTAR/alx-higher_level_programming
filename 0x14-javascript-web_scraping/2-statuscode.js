#!/usr/bin/node
/* Script that displays the status code of a GET request */

const https = require('https');
const url = process.argv[2];

const options = {
  method: 'GET',
  headers: {
    'User-Agent': 'Node.js'
  }
};

const request = https.request(url, options, (response) => {
  console.log(`code: ${response.statusCode}`);
});

request.on('error', (error) => {
  console.log(`Error: ${error.message}`);
});

request.end();
