class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            x = self.q.popleft()
            self.q.append(x)
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


# Another wacky fun solution with constant time push/pop
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class MyStack:
    def __init__(self):
        self.q = deque()
        self.back = None
        self.length = 0
        
    def push(self, x: int) -> None:
        n = Node(x, self.back)
        self.q.append(n)
        self.back = n
        self.length += 1

    def pop(self) -> int:
        x = self.back.data
        self.back = self.back.next
        self.length -= 1
        return x

    def top(self) -> int:
        return self.back.data

    def empty(self) -> bool:
        return self.length == 0