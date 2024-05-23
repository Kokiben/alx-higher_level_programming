#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${filmId}/`;

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error('Error fetching film:', err);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, (charErr, charResponse, charBody) => {
      if (charErr) {
        console.error('Error fetching character:', charErr);
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
