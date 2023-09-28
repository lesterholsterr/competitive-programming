class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.left = self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def append(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.append(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
        elif self.size == self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        else:
            self.size += 1
        self.cache[key] = Node(key, value)
        self.append(self.cache[key])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
