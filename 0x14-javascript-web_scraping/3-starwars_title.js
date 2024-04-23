#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    process.exit(1);
  } else if (response.statusCode !== 200) {
    console.error(`Received code status: ${response.statusCode}`);
    process.exit(1);
  } else {
    const film = JSON.parse(body);

    // Print the title of the movie
    console.log(film.title);
  }
});
