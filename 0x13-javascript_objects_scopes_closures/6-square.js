#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (C) {
    if (C === undefined) {
      this.print();
    } else {
      for (let a = 0; a < this.height; a++) console.log(C.repeat(this.width));
    }
  }
};
