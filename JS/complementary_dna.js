// Complementary DNA
//  KATA LINK: https://www.codewars.com/kata/554e4a2f232cdd87d9000038

// Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and 
// carries the "instructions" for the development and functioning of living organisms.

// If you want to know more: http://en.wikipedia.org/wiki/DNA

// In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
// You have function with one side of the DNA (string, except for Haskell); you need to get the 
// other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

function DNAStrand(dna){
  map = {
    A: 'T',
    G: 'C',
    T: 'A',
    C: 'G',
  };
  
  let result = '';
  for(char of dna) {
    result += map[char];
   }
  return result;
}