#!/usr/bin/node
function factorial (F) {
  if (F < 0) {
    return (-1);
  }
  if (F === 0 || isNaN(F)) {
    return (1);
  }
  return (F * factorial(F - 1));
}

console.log(factorial(Number(process.argv[2])));
