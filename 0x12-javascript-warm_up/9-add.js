#!/usr/bin/node

const firstNum = process.argv[2];
const secondNum = process.argv[3];

function add (a, b) {
  const result = parseInt(a) + parseInt(b);
  return result;
}

console.log(add(firstNum, secondNum));
