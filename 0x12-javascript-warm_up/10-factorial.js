#!/usr/bin/node

const num = process.argv[2];

function fact (a) {
  if (a === 0 || isNaN(a) || a < 0) {
    return 1;
  }
  const result = a * fact(a - 1);
  return result;
}

console.log(fact(parseInt(num)));
