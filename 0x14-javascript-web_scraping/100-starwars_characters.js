#!/usr/bin/node

const rqst = require('request');

const filmId = process.argv[2];
const apUrl = `https://swapi.dev/api/films/${filmId}/`;

rqst(apUrl, (err, response, body) => {
  if (err) {
    console.error('Error fetching film:', err);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;

  characters.forEach(characterUrl => {
    rqst(characterUrl, (charErr, charResponse, charBody) => {
      if (charErr) {
        console.error('Error fetching character:', charErr);
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
