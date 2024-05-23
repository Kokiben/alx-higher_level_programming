#!/usr/bin/node
const rqst = require('request');
const apurl = process.argv[2];

rqst(apurl, (err, rsps) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`code: ${rsps.statusCode}`);
  }
});
