// Persistent Bugger.
// KATA LINK: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

// Write a function, persistence, that takes in a positive parameter num and returns its 
// multiplicative persistence, which is the number of times you must multiply the digits in 
// num until you reach a single digit.

function persistence(num) {
  const digitsOfNum = (no) => {
    res = [];
    while(no > 0) {
      res.push(no % 10)
      no = Math.floor(no / 10)
    };
    return res;
  };
  
  let i = 0;
  while(Math.floor(num/10) > 0) {
    num = digitsOfNum(num).reduce((a, b) => a * b);
    i++;
  }
  
  return i;
}