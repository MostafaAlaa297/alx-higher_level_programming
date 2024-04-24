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
    const tasks = JSON.parse(body);
    let complete = {}
    for (const task of tasks) {
      if (task.completed) {
        complete[task.userId] = (complete[task.userId] || 0) + 1;
	}
      }
      console.log(complete);
    }
});
