# pretty straightforward, no comment
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        cur = [""]
        numToLet = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        }

        def bt(i):
            if i == len(digits):
                ans.append(cur[0])
                return
            letters = numToLet[int(digits[i])]
            for l in letters:
                cur[0] += l
                bt(i+1)
                cur[0] = cur[0][:-1]
        
        if len(digits) == 0:
            return []
        bt(0)
        return ans