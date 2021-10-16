// Unique In Order
// KATA LINK: https://www.codewars.com/kata/54e6533c92449cc251001667

// Implement the function unique_in_order which takes as argument a sequence and returns a 
// list of items without any elements with the same value next to each other and preserving 
// the original order of elements.

function uniqueInrder(iterable) {
  return [...iterable].reduce((prev, curr, _, arr) =>
    prev[prev.length - 1] !== curr ? prev.push(curr) && prev : prev,
  []);
}