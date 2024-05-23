#!/usr/bin/node
const fileSyst = require('fs');
const fPath = process.argv[2];

fileSyst.readFile(fPath, 'utf8', (err, cott) => {
  if (err) {
    console.error(err);
  } else {
    console.log(cott);
  }
});
