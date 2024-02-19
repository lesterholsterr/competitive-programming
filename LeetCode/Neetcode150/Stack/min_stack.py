# Overall: Pretty straightforward. Wrote out an example and implemented it
# if       stack = [5, 3, 4, 1, 2]
# then min value = [5, 3, 3, 1, 1]
# Leaps
# - How can we remember the min value at each 'depth' in the stack? (use another stack)

class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minval = min(self.getMin(), val) if len(self.minstack) > 0 else val
        self.minstack.append(minval)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
