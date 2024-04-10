#!/usr/bin/node
module.exports = class Rectangle {
  constructor (wid, heig) {
    if (wid > 0 && heig > 0) { [this.width, this.height] = [wid, heig]; }
  }
};
