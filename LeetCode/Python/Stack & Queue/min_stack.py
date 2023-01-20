class MinStack(object):

    def __init__(self, stack=[], minstack=[], size=0):
        self.stack = []
        self.minstack = []
        self.size = -1
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.size == -1:
            self.minstack.append(val)
        elif self.minstack[self.size] > val:
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[self.size])
        self.size += 1
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minstack.pop()
        self.size -= 1
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[self.size]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[self.size]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()