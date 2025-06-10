#!/usr/bin/node
const args = process.argv;
if (args.lenght <= 2) {
  console.log('Missing number of occurrences');
} else if (args[2] >= 0) {
  let l = 0;
  while (l < args[2]) {
    console.log('C is fun');
    l++;
  }
}
