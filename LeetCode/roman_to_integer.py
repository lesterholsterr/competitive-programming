class Solution(object):
  def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    lastDigit = 0
    for i in range(len(s)-1, -1, -1):
      x = vals[s[i]]
      if x < lastDigit:
        sum -= x
        lastDigit = x
      else: 
        sum += x
        lastDigit = x
    return sum