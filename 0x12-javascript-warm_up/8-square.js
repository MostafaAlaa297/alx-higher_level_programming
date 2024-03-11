#!/usr/bin/node

const x = process.argv[2];

if (!Number.isInteger(parseInt(x)) || x < 1) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
