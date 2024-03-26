# thoughts
# - similar to house robber and climbing stairs

# Initial - very brute forcey so TLE
class Solution:
    def numDecodings(self, s: str) -> int:
        valid = set()
        for i in range(1, 27):
            valid.add(str(i))

        def legal(x):
            return x in valid

        if len(s) == 0:
            return 1
        elif len(s) == 1:
            return 1 if legal(s) else 0
        else:
            n = 0
            if legal(s[0]):
                n += self.numDecodings(s[1:])
            if legal(s[0:2]):
                n += self.numDecodings(s[2:])
            return n

# figured it out
class Solution:
    def numDecodings(self, s: str) -> int:
        valid = set()
        for i in range(1, 27):
            valid.add(str(i))

        def legal(x):
            return x in valid

        ans = [0] * len(s)
        if s[-1] != "0":
            ans[-1] = 1
        ans.append(1)  # for case (*)

        for i in range(len(s)-2, -1, -1):
            if legal(s[i]):
                ans[i] += ans[i+1]
            if legal(s[i:i+2]):
                ans[i] += ans[i+2]  # case (*) - when i+2 out of bounds
        return ans[0]

# Again but with O(1) memory
class Solution:
    def numDecodings(self, s: str) -> int:
        valid = set()
        for i in range(1, 27):
            valid.add(str(i))
        
        def legal(x):
            return x in valid
        
        a = 1 if legal(s[-1]) else 0
        b = 1

        for i in range(len(s)-2, -1, -1):
            tmp = 0
            if legal(s[i]):
                tmp += a
            if legal(s[i:i+2]):
                tmp += b
            a, b = tmp, a
        return a