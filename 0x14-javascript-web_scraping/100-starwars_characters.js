#!/usr/bin/node

const rqst = require('request');

const filmId = process.argv[2];
const apUrl = `https://swapi.dev/api/films/${filmId}/`;

rqst(apUrl, (err, rspse, ody) => {
  if (err) {
    console.error('Error fetching film:', err);
    return;
  }

  const jata = JSON.parse(ody);
  const chters = jata.chters;

  chters.forEach(characterUrl => {
    rqst(characterUrl, (charErr, charRspse, charBody) => {
      if (charErr) {
        console.error('Error fetching character:', charErr);
        return;
      }

      const chctrData = JSON.parse(charBody);
      console.log(chctrData.name);
    });
  });
});
