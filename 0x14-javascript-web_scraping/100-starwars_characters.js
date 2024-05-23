#!/usr/bin/node

const rqst = require('request');

const filmId = process.argv[2];
const apUrl = `https://swapi.dev/api/films/${filmId}/`;

rqst(apUrl, (err, response, resbody) => {
  if (err) {
    console.error('Error fetching film:', err);
    return;
  }

  const data = JSON.parse(resbody);
  const characters = data.characters;

  characters.forEach(characterUrl => {
    rqst(characterUrl, (charErr, charResponse, charBody) => {
      if (charErr) {
        console.error('Error fetching character:', charErr);
        return;
      }

      const charInfo = JSON.parse(charBody);
      console.log(charInfo.name);
    });
  });
});
