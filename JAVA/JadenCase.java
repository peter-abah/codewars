// Jaden Casing Strings
// KATA LINK: https://www.codewars.com/kata/5390bac347d09b7da40006f6

/*
  Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) 
  and After Earth (2013). Jaden is also known for some of his philosophy that he delivers 
  via Twitter. When writing on Twitter, he is known for almost always capitalizing every word.
  For simplicity, you'll have to capitalize each word, check out how contractions are expected 
  to be in the example below.

  Your task is to convert strings to how they would be written by Jaden Smith. 
  The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he 
  originally typed them.
*/

public class JadenCase {
  public String toJadenCase(String phrase) {
    if (phrase != null && phrase.length() > 0) {
      String[] strArr = phrase.split(" ");
      String[] outArr = new String[strArr.length];
      
      for (int i = 0; i < strArr.length; i++) {
        String s = strArr[i];
        outArr[i] = s.replace(s.charAt(0), Character.toUpperCase(s.charAt(0)));
      }
    
      return String.join(" ", outArr);
    }
  
  return null;
  }

}