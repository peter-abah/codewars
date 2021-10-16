# Hamming Numbers
# KATA LINK: https://www.codewars.com/kata/526d84b98f428f14a60008da

# A Hamming number is a positive integer of the form 2i3j5k, for some non-negative integers i, j, and k.
# Write a function that computes the nth smallest Hamming number.

# Specifically:
# The first smallest Hamming number is 1 = 203050
# The second smallest Hamming number is 2 = 213050
# The third smallest Hamming number is 3 = 203150
# The fourth smallest Hamming number is 4 = 223050
# The fifth smallest Hamming number is 5 = 203051


def hamming(n):
  h = [1]
  i2, i3, i5 = 0, 0, 0
  for i in range(n-1):
    x = min( 2*h[i2], 3*h[i3], 5*h[i5] )
    h.append(x)
    if x >= 2*h[i2]: i2 += 1
    if x >= 3*h[i3]: i3 += 1
    if x >= 5*h[i5]: i5 += 1
  return h[-1]