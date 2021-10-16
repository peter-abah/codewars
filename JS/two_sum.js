// Two Sum
// KATA LINK: https://www.codewars.com/kata/52c31f8e6605bcc646000082

function twoSum(numbers, target) {
  cache = {};
  let res = [];

  numbers.forEach((e, i) => {
    if (cache[target-e] !== undefined)
      res = [i, cache[target-e]];
    cache[e] = i;
  });
  return res;
}