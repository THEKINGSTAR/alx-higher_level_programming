#!/usr/bin/node

const nfound = 'No argument';
const args = process.argv;

if (args[2] !== undefined) {
  console.log(args[2]);
} else if (args[2] === undefined) {
  console.log(nfound);
}
