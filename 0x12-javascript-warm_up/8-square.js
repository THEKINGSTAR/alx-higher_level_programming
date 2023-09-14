#!/usr/bin/node

const args = process.argv;
const x = parseInt(args[2]);

if (!Number.isInteger(x) || typeof x === 'string') {
  console.log('Missing size');
} else {
  let l = 0;
  while (l < args[2]) {
    let lin = '';
    for (let ll = 0; ll < args[2]; ll++) {
      lin += 'X';
    }
    console.log(lin);

    l++;
  }
}
