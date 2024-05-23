#!/usr/bin/node
const fileSys = require('fs');
const rqst = require('request');

const apurl = process.argv[2];
const fPath = process.argv[3];

rqst(apurl).pipe(fileSys.createWriteStream(fPath));
