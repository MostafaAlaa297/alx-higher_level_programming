#!/usr/bin/node

const request = require('request');
const input = process.argv;

request(input[2], function (error, response) {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  console.log(response.statusCode);
});
