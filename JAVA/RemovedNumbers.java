// Is My Friend Cheating
// KATA LINK: https://www.codewars.com/kata/5547cc7dcad755e480000004

/* A friend of mine takes the sequence of all numbers from 1 to n (where n > 0).
  Within that sequence, he chooses two numbers, a and b.

  He says that the product of a and b should be equal to the sum of all numbers in the sequence, 
  excluding a and b.
  Given a number n, could you tell me the numbers he excluded from the sequence?

  The function takes the parameter: n (n is always strictly greater than 0) and returns an 
  array or a string (depending on the language) of the form:
  [(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or or [{a, b}, ...]
*/


import java.util.*;

public class RemovedNumbers {
  
  public static ArrayList<long[]> removNb(long n) {
      ArrayList<long[]> res = new ArrayList<long[]>();
      long sum = ( n*n + n)/2;
    
      for(long a = 1; a <= n; a++) {
          long mod = (sum - a) % (a+1);
          if (mod == 0) {
              long b = (sum - a) / (a+1);
              if (b <= n) res.add(new long[] { a, b });
          }
      }
      return res;
  }
}