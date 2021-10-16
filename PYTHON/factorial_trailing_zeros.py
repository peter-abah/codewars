# Number of trailing zeros of N!
# KATA LINK: https://www.codewars.com/kata/52f787eb172a8b4ae1000a34

# Write a program that will calculate the number of trailing zeros in a factorial of a given number.

# N! = 1 * 2 * 3 * ... * N

# Be careful 1000! has 2568 digits...


def zeros(n):
  m = n
  count = 0
  m_5 = 5
  
  while m_5 < n:
    m_5 *= 5
  m_5 //= 5

  while m_5 > 5:
    count += m//m_5
    m_5 /= 5
  
  return n//5 + count