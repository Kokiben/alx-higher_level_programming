#!/usr/bin/node
exports.esrever = function (list) {
  let leng = list.length - 1;
  let a = 0;
  while ((leng - a) > 0) {
    const x = list[leng];
    list[leng] = list[a];
    list[a] = x;
    a++;
    leng--;
  }
  return list;
};
