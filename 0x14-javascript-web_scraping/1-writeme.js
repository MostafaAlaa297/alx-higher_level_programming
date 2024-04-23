#!/usr/bin/node

const fs = require('fs');

if (process.argv.length < 3) {
  console.error('Usage: node 0-readme.js <file_path>');
  process.exit(1);
}

const file = process.argv[2];
const input = process.argv[3];

fs.writeFile(file, input, (err) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
});
