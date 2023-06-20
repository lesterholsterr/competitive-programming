class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Overall: Once you convince yourself that the problem can be solved using 2 pointers, it becomes rather trivial
        # Leaps
        # - If max + min > target, then there is no way min will be one of the 2 numbers
        # - Same for opposite
        
        l = len(numbers)
        small = 0
        big = l-1

        while True:
            sum = numbers[small] + numbers[big]
            if sum == target:
                return [small+1, big+1]
            elif sum >= target:
                big -= 1
            elif sum <= target:
                small += 1
