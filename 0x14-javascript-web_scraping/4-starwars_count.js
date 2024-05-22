#!/usr/bin/node

const rqt = require('request');
const apUrl = process.argv[2];
const charId = '18';
let cont = 0;

rqt.get(apUrl, (err, rsps, rqtdata) => {
  if (err) {
    console.log(err);
  } else {
    const chardata = JSON.parse(rqtdata);
    chardata.results.forEach((movie) => {
      movie.characters.forEach((character) => {
        if (character.includes(charId) || character.includes(`/people/${charId}/`)) {
          cont += 1;
        }
      });
    });
    console.log(cont);
  }
});
