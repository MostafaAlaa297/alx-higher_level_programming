#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    process.exit(1);
  } else if (response.statusCode !== 200) {
    console.error(`Received code status: ${response.statusCode}`);
    process.exit(1);
  } else {
    const films = JSON.parse(body);
    let count = 0;

    for (const film of films.results) {
      if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    }

    // Print the title of the movie
    console.log(count);
  }
});
