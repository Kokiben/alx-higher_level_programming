#!/usr/bin/node

const rqt = require('request');

const apUrl = process.argv[2];

const charId = '18'; // Char ID of Wedge Antilles

// Fun to count the num of movies where char is present
function contMoviesWithChar(fms) {
    let cont = 0;
    fms.forEach(fm => {
        if (fm.characters.includes(`https://swapi-api.alx-tools.com/api/people/${charId}/`)) {
            cont++;
        }
    });
    return cont;
}

// Making a request to retrieve information about each film
rqt(apUrl, (err, rsps, rpsdata) => {
    if (err) {
        console.error(err);
        return;
    }
    
    console.log(rsps); // Log the response object

    if (rsps.statusCode !== 200) {
        console.error(`Failed to retrieve data. Status code: ${rsps.statusCode}`);
        return;
    }

    const fms = JSON.parse(rspsdata).results; // list of films from response

    // Counting num of movies where char is present
    const movCont = contMoviesWithChar(fms);
    console.log(movCont);
});
