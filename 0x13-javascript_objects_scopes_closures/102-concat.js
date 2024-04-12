#!/usr/bin/node
const Fils = require('fs');

const FirstArgm = Fils.readFileSync(process.argv[2]).toString();
const SecondArgm = Fils.readFileSync(process.argv[3]).toString();
Fils.writeFileSync(process.argv[4], FirstArgm + SecondArgm);
