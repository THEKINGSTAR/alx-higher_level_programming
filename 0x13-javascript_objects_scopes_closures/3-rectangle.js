#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!(w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h))) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let l = 0; l < this.height; l++) {
      let row = '';
      for (let ll = 0; ll < this.width; ll++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}

module.exports = Rectangle;
