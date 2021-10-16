// Roman Numerals Decoder
// KATA LINK: https://www.codewars.com/kata/51b6249c4612257ac0000005

// Create a function that takes a Roman numeral as its argument 
// and returns its value as a numeric decimal integer. 
// You don't need to validate the form of the Roman numeral.

function solution(roman){
  map = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };
  
  return [...roman].reduce((num, char) => {
    i = map[char];
    return num > 0 && num < i ? i - num : i + num;
  }, 0)
}