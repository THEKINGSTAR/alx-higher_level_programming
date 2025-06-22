#!/usr/bin/node
/* Script that displays the status code of a GET request */
/*
 * The first argument is the URL to request (GET)
 * The status code must be printed like this: code: <status code>
 * You must use the module request
 */
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
