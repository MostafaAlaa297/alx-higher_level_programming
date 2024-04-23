#!/usr/bin/node

const fs = require("fs");

if (process.argv.length != 3){
	console.error("Usage: node 0-readme.js <file_path>");
	process.exit(1);
}

const file = process.argv[2];

fs.readFile(file, "utf-8", (err, data) => {
	if (err){
		console.error(err);
		process.exit(1);
	}
	console.log(data);
});
