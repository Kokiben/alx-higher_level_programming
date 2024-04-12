#!/usr/bin/node
const lst = require('./100-data.js').list;
console.log(lst);
console.log(lst.map((itm, indx) => itm * indx));
