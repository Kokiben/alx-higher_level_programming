#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const X = Number(process.argv[2]);
  let a = 0;
  while (a < X) {
    console.log('C is fun');
    a++;
  }
}
