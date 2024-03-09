# Overall: Brute force was intuitive but using stack to optimize was not clear at intuitive to me.
# Strategy is to only look in one direction (eg. left to right). Idk how it would occur to someone
# to try stack. And even if you do, algorithm still seems unintuitive.

# Edit: Helpful dude in the comments explained how brute force can be reduced to stack solution:
# - The inefficiency of the brute force solution is the re-scanning of both left and right
# - Notice by storing *increasing* bars in a stack, we can remove the right scan
#       - ^This is still a pretty big mental leap...
# - When popping rectangles in increasing order, no left scan is needed.
# - Intuitively, we can remove the left scan by remembering the index of the last popped rectangle

# Initial Solution
# O(n^2) brute force times out on one of the last cases
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = max(heights)

        def findArea(i, h):
            area = 0
            l, r = i, i+1
            while l >= 0 and heights[l] >= h:
                area += h
                l -= 1
            while r < len(heights) and heights[r] >= h:
                area += h
                r += 1
            return area

        for i in range(len(heights)):
            left, right = 0, 0
            if i != 0:
                left = findArea(i, min(heights[i], heights[i-1]))
            if i != len(heights)-1:
                right = findArea(i, min(heights[i], heights[i+1]))
            largest = max(largest, left, right)

        return largest

# Neetcode Solution


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []

        for i in range(len(heights)):
            start = i
            while len(stack) != 0 and stack[-1][1] > heights[i]:
                j, h = stack.pop()
                largest = max(largest, h * (i-j))
                start = j
            stack.append((start, heights[i]))

        l = len(heights)
        while len(stack) != 0:
            j, h = stack.pop()
            largest = max(largest, h * (l-j))

        return largest
