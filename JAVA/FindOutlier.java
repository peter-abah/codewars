// Find tHE Parity Outlier
// KATA LINK: https://www.codewars.com/kata/5526fc09a1bbd946250002dc

/*
  You are given an array (which will have a length of at least 3, but could be very large) 
  containing integers. The array is either entirely comprised of odd integers or 
  entirely comprised of even integers except for a single integer N. Write a method that 
  takes the array as an argument and returns this "outlier" N.
*/

public class FindOutlier{
  static int find(int[] integers){
    int odd = 0;
    int even = 0;
    int curEven = 0;
    int curOdd = 0;
  
    for (int i: integers) {
      if ( i % 2 == 0 ) {
        curEven = i;
        even++;
      }
      else {
        curOdd = i;
        odd++;
      }
      if (even == 1 && odd > 1) return curEven;
      else if ( odd == 1 && even > 1) return curOdd;
    }
   return 0;         
}}