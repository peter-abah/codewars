// Duplicate Encoder
// KATA LINK: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

/*
  The goal of this exercise is to convert a string to a new string where each character 
  in the new string is "(" if that character appears only once in the original string, 
  or ")" if that character appears more than once in the original string. Ignore 

  capitalization when determining if a character is a duplicate.
*/

import java.util.*;

public class DuplicateEncoder {
  static String encode(String word){
    word = word.toLowerCase();
    var map = new HashMap<Character, Integer>();
    
    for (int i = 0; i < word.length(); i++) {
      char c = word.charAt(i);
      if (map.containsKey(c)) {
        map.put(c, map.get(c) + 1);
      }
      else {
        map.put(c, 1);
      }
    }
    var out = new StringBuilder();
    for (int i = 0; i < word.length(); i++) {
      if ( map.get(word.charAt(i)) > 1 )
        out.append(')');
      else out.append('(');
    }
    return out.toString();
  }
}