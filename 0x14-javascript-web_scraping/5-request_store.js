#!/usr/bin/node

const request = require('request');
const fs = require("fs")
const url = process.argv[2];
const file = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    process.exit(1);
  } else if (response.statusCode !== 200) {
    console.error(`Received code status: ${response.statusCode}`);
    process.exit(1);
  } else {
    fs.writeFile(file, body, (err) => {
	    if (err) {
		    console.error(err);
		    process.exit(1);
	    }
    });
  }
});
