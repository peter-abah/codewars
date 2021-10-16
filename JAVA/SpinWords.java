// Stop gninnipS My sdroW!
// KATA LINK: https://www.codewars.com/kata/5264d2b162488dc400000001

/*
  Write a function that takes in a string of one or more words, and returns the same string, 
  but with all five or more letter words reversed (like the name of this kata).

  Strings passed in will consist of only letters and spaces.
  Spaces will be included only when more than one word is present.
*/

public class SpinWords {

  public String spinWords(String sentence) {
    String[] words = sentence.split(" ");
    String res = "";
  
    for(String s: words) {
      if (s.length() >= 5) {
        String w = "";
        for(int i = s.length() -1; i >= 0; i--) {
          w += s.charAt(i);
        }
        res = res + w;
      }
      else res = res + s;
      res += " ";
    }
    return res.toString().trim();
  }
}