#!/usr/bin/node

const square = require('./5-square.js');

class Square extends square {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    let st = c;
    if (c === undefined) {
      st = 'X';
    }
    for (let p = 0; p < this.size; p++) {
      let lin = '';
      for (let l = 0; l < this.size; l++) {
        lin += st;
      }
      console.log(lin);
    }
  }
}
module.exports = Square;
