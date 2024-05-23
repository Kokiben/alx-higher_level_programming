#!/usr/bin/node
const fileSys = require('fs');
const fPath = process.argv[2];
const fCott = process.argv[3];

fileSys.writeFile(fPath, fCott, (err) => {
  if (err) {
    console.error(err);
  }
});
