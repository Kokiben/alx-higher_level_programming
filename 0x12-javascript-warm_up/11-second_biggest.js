#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const Ser = process.argv.slice(2).map(Number);
  const Sec = Ser.sort(function (c, d) { return c - d; })[1];
  console.log(Sec);
}
