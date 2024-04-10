#!/usr/bin/node
let argmt = 0;

exports.logMe = function (item) {
  console.log(argmt + ': ' + item);
  argmt++;
};
