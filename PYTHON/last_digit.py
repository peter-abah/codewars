# Last Digit of a Large Number
# KATA LINK: https://www.codewars.com/kata/5511b2f550906349a70004e1

# Define a function that takes in two non-negative integers aaa and bbb and returns the last 
#   decimal digit of aba^bab. Note that aaa and bbb may be very large!

# For example, the last decimal digit of 979^797 is 999, since 97=47829699^7 = 478296997=4782969. 
# The last decimal digit of (2200)2300({2^{200}})^{2^{300}}(2200)2300, 
#   which has over 109210^{92}1092 decimal digits, is 666. Also, please take 000^000 to be 111.


def last_digit(n1, n2):
  powers = { 
    0 : [0],
    1 : [1],
    2 : [6, 2, 4, 8],
    3 : [1, 3, 9, 7],
    4 : [6, 4],
    5 : [5],
    6 : [6],
    7 : [1, 7, 9, 3],
    8 : [6, 8, 4, 2],
    9 : [1, 9] 
  }

  if n2 == 0:
    return 1
  i = (n2 % len(powers[n1%10]))
  return powers[n1%10][i]