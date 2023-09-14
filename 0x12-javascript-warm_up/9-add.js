#!/usr/bin/node

const args = process.argv;

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

const f = parseInt(args[2]);
const s = parseInt(args[3]);
add(f, s);
