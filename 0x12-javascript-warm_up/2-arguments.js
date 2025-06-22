#!/usr/bin/node

const found = 'Argument found';
const nfound = 'No argument';
const mfound = 'Arguments found';

if (process.argv.length === 2) {
  console.log(nfound);
} else if (process.argv.length === 3) {
  console.log(found);
} else {
  console.log(mfound);
}
