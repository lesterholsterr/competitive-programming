class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.k = k
        self.stream = deque(nums)

    def add(self, val: int) -> int:
        if len(self.stream) == 0:
            self.stream.append(val)
        elif val >= self.stream[-1]:
            self.stream.append(val)
        else:
            for i in range(len(self.stream)):
                if val <= self.stream[i]:
                    self.stream.insert(i, val)
        return self.stream[-(self.k)]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
