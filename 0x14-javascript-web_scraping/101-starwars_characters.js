#!/usr/bin/node

const rqst = require('request');

const filmId = process.argv[2];
const apUrl = `https://swapi.dev/api/films/${filmId}/`;

rqst(apUrl, (err, response, resbody) => {
  if (err) {
    console.error('Error fetching film:', err);
    return;
  }

  const dat = JSON.parse(resbody);
  const chrctr = dat.characters;
  fetchChrctrs(chrctr, 0);
});

const fetchChrctrs = (chrctr, elem) => {
  if (elem === chrctr.length) {
    return;
  }

  rqst(chrctr[elem], (err, response, resbody) => {
    if (err) {
      console.error('Error fetching character:', err);
      return;
    }

    const charInfo = JSON.parse(resbody);
    console.log(charInfo.name);
    fetchChrctrs(chrctr, elem + 1);
  });
};
