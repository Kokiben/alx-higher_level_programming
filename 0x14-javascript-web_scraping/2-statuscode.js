#!/usr/bin/node

const req = require('request');  // Renaming 'request' to 'req'
const targetUrl = process.argv[2];  // Renaming 'url' to 'targetUrl'

req.get(targetUrl, (err, res) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
