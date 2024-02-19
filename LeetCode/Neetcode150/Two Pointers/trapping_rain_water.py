# Overall: Algorithm makes sense once I see it, but very unintuitive path to get there
# Each index can hold the difference of the (minimum of the maximum left and right heights) and the (current height)

# O(n) memory solution
class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        maxsofar = 0
        for i in range(1, len(height)):
            maxsofar = max(maxsofar, height[i-1])
            max_left[i] = maxsofar
        
        max_right = [0] * len(height)
        maxsofar = 0
        for i in range(len(height) - 2, -1, -1):
            maxsofar = max(maxsofar, height[i+1])
            max_right[i] = maxsofar
        
        water = 0
        for i in range(len(height)):
            water += max(0, min(max_left[i], max_right[i]) - height[i])

        return water

# Constant memory solution
# The additional observation needed is that you can solve the problem without knowing where the
# maximums are as long as you keep track of the minimums (since we take a minimum of the max and min anyways
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        water = 0

        while l != r:
            if max_l <= max_r:
                l += 1
                max_l = max(max_l, height[l])
                water += max(0, max_l - height[l])
            else:
                r -= 1
                max_r = max(max_r, height[r])
                water += max(0, max_r - height[r])

        return water