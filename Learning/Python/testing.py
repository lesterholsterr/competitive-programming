def largestRectangleArea(heights) -> int:
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

print(largestRectangleArea([2,1,2]))
