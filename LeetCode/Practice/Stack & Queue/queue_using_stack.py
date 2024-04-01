class MyQueue(object):

    def __init__(self):
        self.in_stk = []
        self.out_stk = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.in_stk.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.out_stk.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())
        return self.out_stk[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.in_stk and not self.out_stk