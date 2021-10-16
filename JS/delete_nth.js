// Delete occurrences of an element if it occurs more than n times
// KATA LINK: https://www.codewars.com/kata/554ca54ffa7d91b236000023

function deleteNth(arr,n){
  res = [];
  arr.forEach((e) => res.filter( x => x === e).length < n && res.push(e));
  return res;
}