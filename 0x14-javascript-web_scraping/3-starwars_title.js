#!/usr/bin/node

const rqst = require('request');

const movId = process.argv[2];
const apUrl = `https://swapi-api.alx-tools.com/api/films/${movId}`;

rqst(apUrl, (err, rspons, rpsdata) => {
  if (err) {
    console.error(err);
    return;
  }

  if (rspons.statusCode !== 200) {
    console.error(`Failed to retrieve data. Status code: ${rspons.statusCode}`);
    return;
  }

  const movie = JSON.parse(rpsdata);
  console.log(movie.title);
});
