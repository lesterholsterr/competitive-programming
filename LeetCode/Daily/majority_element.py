# O(n) memory solution is simple
# O(1) memory is much neater. Think of the array as a game of tug-of-war between the majority element
# and everyone else. We are guaranteed that the net 'tugs' will go in favour of the majority element.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num, freq = 0, 0
        for n in nums:
            if freq <= 0:
                num = n
            freq += 1 if n == num else -1
        return num
