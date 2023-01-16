class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(numbers)
        small = 0
        big = l-1

        while True:
            sum = numbers[small] + numbers[big]
            if sum == target:
                return[small+1, big+1]
            elif sum >= target:
                big -= 1
            elif sum <= target:
                small += 1