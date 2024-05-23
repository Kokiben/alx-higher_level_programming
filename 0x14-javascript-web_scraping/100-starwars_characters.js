#!/usr/bin/node

const rqst = require('request');

const filmd = process.argv[2];
const apurl = `https://swapi.dev/api/films/${filmd}/`;

rqst(apurl, (err, rspse, addata) => {
  if (err) {
    console.error('Error fetching movie:', err);
    return;
  }

  const jiji = JSON.parse(addata);
  const charjiji = jiji.charjiji;

  charjiji.forEach(ractrr => {
    rqst(ractrr, (charErr, charRsps, chardat) => {
      if (charErr) {
        console.error('Error fetching character:', charErr);
        return;
      }

      const Jasonchar = JSON.parse(chardat);
      console.log(Jasonchar.name);
    });
  });
});
