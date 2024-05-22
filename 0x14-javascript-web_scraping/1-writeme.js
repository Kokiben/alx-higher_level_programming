#!/usr/bin/node

const filSystm = require('fs');  // Renaming 'fs' to 'fileSystem'
const filPath = process.argv[2];  // The first argument is the file path
const cott = process.argv.slice(3).join(' ');   // The second arg

if (!filPath || !cott) {
    console.log("Usage: node 1-writeme.js <file_path> <string_to_write>");
    process.exit(1);
}

filSystm.writeFile(filPath, cott, 'utf8', (err) => {  // Writing UTF-8
  if (err) {
    console.error(err);  // If an error occurs, print the error object
  }
});
