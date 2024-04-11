#!/usr/bin/node
function add (a, b) {
  const D = a + b;
  console.log(D);
}

add(Number(process.argv[2]), Number(process.argv[3]));
