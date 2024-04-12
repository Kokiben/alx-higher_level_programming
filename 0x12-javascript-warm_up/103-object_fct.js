#!/usr/bin/node
let miobjt = {
  type: 'object',
  value: 12
};
console.log(miobjt);
myObject.incr = function () {
  this.value++;
};
myObject.incr();
console.log(miobjt);
myObject.incr();
console.log(miobjt);
myObject.incr();
console.log(miobjt);
