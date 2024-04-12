#!/usr/bin/node
const Dct = require('./101-data').dict;

const Totlst = Object.entries(Dct);
const vas = Object.values(Dct);
const vasuniqu = [...new Set(vas)];
const NDct = {};
for (const L in vasuniqu) {
  const Lst = [];
  for (const M in Totlst) {
    if (Totlst[M][1] === vasuniqu[L]) {
      Lst.unshift(Totlst[M][0]);
    }
  }
  NDct[vasuniqu[L]] = Lst;
}
console.log(NDct);
