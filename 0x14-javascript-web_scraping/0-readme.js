#!/usr/bin/node

const fileSystem = require('fs');  // Renaming 'fs' to 'fileSystem'
const filePath = process.argv[2];  // Renaming 'filename' to 'filePath'

fileSystem.readFile(filePath, 'utf8', (err, data) => {  // Using 'fileSystem'
  if (err) {
    console.log(err);  // Using 'err' instead of 'error'
  } else {
    console.log(data);  // Using 'data' instead of 'content'
  }
});
