class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = 0
        open = []
        for b in s:
            if b == '(' or b == '[' or b == '{':
                open.append(b)
                count += 1
            else:
                if len(open) == 0:
                    return False
                e = open[count-1]
                if b == ')' and e != '(':
                    return False
                elif b == ']' and e != '[':
                    return False
                elif b == '}' and e != '{':
                    return False
                else:
                    open.pop(count-1)
                    count -= 1
        return True if len(open) == 0 else False