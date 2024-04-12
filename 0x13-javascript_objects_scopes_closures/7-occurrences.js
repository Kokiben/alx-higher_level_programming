#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((cou, crrnt) => crrnt === searchElement ? cou + 1 : cou, 0);
};
