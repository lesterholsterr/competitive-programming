class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        # Overall: Fairly simple
        # Leaps
        # - An operator pops 2 values from the array and appends their result

        res = []
        for token in tokens:
            if token == '+':
                x = res.pop()
                y = res.pop()
                res.append(y + x)
            elif token == '-':
                x = res.pop()
                y = res.pop()
                res.append(y - x)
            elif token == '*':
                x = res.pop()
                y = res.pop()
                res.append(y * x)
            elif token == '/':
                x = res.pop()
                y = res.pop()
                res.append(int(y / x))
            else:
                res.append(int(token))
        return res[0]