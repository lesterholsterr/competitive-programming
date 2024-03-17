# thoughts
# - came close, realized the data structure only needs to store decreasing elements
#       - got to this step by considering how to solve the problem if the array was
#         increasing versus decreasing
# - did not realize in a decreasing q, leftmost element is the max
#       - biggest leap is to go from here to the actual algorithm
# - consider the queue should track decreasing elements in a given window
# - so it needs to store indexes to know when to drop the left elements

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        ans = []
        info = collections.deque()
        info.append(0)  # <- just append the index!

        for i in range(1, len(nums)):
            while info and nums[i] > nums[info[-1]]:
                info.pop()
            info.append(i)

            while info[0] < i-k+1:  # <- offby1 mistake
                info.popleft()
            if i >= k-1:
                ans.append(nums[info[0]])

        return ans
