#!/usr/bin/node
/* script that writes a string to a file */
const file = process.argv[2];
const fs = require('fs');
const string = process.argv[3];

fs.writeFile(file, string, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
