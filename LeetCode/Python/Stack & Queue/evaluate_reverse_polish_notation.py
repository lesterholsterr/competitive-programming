class Solution:
    def evalRPN(self, tokens):
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
