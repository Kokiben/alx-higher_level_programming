#!/usr/bin/node
module.exports = class Rectangle {
  constructor (wid, heig) {
    if (wid > 0 && heig > 0) { [this.width, this.height] = [wid, heig]; }
  }

  print () {
    for (let a = 0; a < this.height; a++) console.log('X'.repeat(this.width));
  }
};
