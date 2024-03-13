#!/usr/bin/node

const ParentSquare = require('./5-square.js');

class Square extends ParentSquare {
  charPrint (c) {
    if (c === undefined) {
      for (let i = 0; i < this.size; i++) {
        console.log('X'.repeat(this.size));
      }
    } else {
      for (let i = 0; i < this.size; i++) {
        console.log(c.repeat(this.size));
      }
    }
  }
}

module.exports = Square;
