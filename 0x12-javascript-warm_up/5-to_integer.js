#!/usr/bin/node
const mynumber = Math.floor(Number(process.argv[2]));
console.log(isNaN(mynumber) ? 'Not a number' : `My number: ${mynumber}`);
