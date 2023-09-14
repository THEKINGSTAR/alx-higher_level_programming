#!/usr/bin/node

const args = process.argv;
const x = parseInt(args[2], 10);

if (!Number.isInteger(x) || typeof x === 'string') {
  console.log('Not a number');
} else {
  console.log('My number: ' + x);
}
