#!/usr/bin/node

const rqt = require('request');
const filSys = require('fs');
const apUrl = process.argv[2];
const fl = process.argv[3]; // Keeping 'file' as is

rqt(apUrl, (err, rsps, rpsdata) => {
  if (err) {
    console.log(err);
  } else {
    filSys.writeFile(fl, rpsdata, 'utf8', (err) => {
      if (err) {
        console.log(err);
      } else {
        console.log(`File "${fl}" has been saved.`);
      }
    });
  }
});
