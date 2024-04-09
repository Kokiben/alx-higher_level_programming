#!/usr/bin/node
const argsLength = process.argv.length;

switch (argsLength) {
    case 2:
        console.log("No argument");
        break;
    case 3:
        console.log("Argument found");
        break;
    default:
        console.log("Arguments found");
}
