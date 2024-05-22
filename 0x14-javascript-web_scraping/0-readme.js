#!/usr/bin/node
"""reads and prints the content of a file"""
const fls = require('fls');

const filePath = process.argv[2];

if (!filePath) {
    console.log("Usage: node 0-readme.js <file_path>");
    process.exit(1);
}

fls.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});
