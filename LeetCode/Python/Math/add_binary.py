class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Copied solution from https://leetcode.com/problems/add-binary/solutions/279879/python-easy-to-understand/?languageTags=python
        a = list(a)
        b = list(b)
        carry = 0
        result = ""

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            result += str(carry % 2)
            carry //= 2
        
        return result[::-1]