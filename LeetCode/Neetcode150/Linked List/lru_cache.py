# Overall: The data structures used came naturally based on the problem requirements.
#          Could have abstracted the "remove node" and "append node" functions as helpers.
# Leaps
# - How do I implement get() in constant time? (obviously need hashing)
# - How do I implement put() in constant time? Need to remove an arbitrary element from an ordered list
#   and append it. (obviously need a doubly LL)
# - Realize that evicting a node should update the hashmap, meaning the node needs to contain a key
#   in addition to a value (to remove the key-value pair from a hashmap, you need the key)

# Initial Solution: 45 minutes, but it works!
class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.lru = None # linked list head 
        self.mru = None # linked list tail
        self.hash = {}

    def get(self, key: int) -> int:
        if key in self.hash:
            n = self.hash[key]
            # remove node from existing position
            if not n.next:
                return n.data[1]
            elif not n.prev:
                self.lru = self.lru.next
                self.lru.prev = None
            else:
                n.prev.next = n.next
                n.next.prev = n.prev

            # insert node to end of LL
            self.mru.next = n
            n.prev = self.mru
            n.next = None
            self.mru = self.mru.next
            
            return n.data[1]

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.hash[key].data = (key, value)
            self.get(key) # This will update the cache

        elif self.size != self.capacity:
            if not self.lru:
                self.lru = Node((key, value), None, None)
                self.mru = self.lru
            else:
                self.mru.next = Node((key, value), None, self.mru)
                self.mru = self.mru.next
            
            self.size += 1
            self.hash[key] = self.mru
            
        else:
            # Evict LRU
            del self.hash[self.lru.data[0]]
            self.lru = self.lru.next

            # Edge case: LRU capacity is 1. We revert to an empty cache and add a new node.
            if not self.lru:
                self.lru = Node((key, value), None, None)
                self.mru = self.lru
            else:
                self.lru.prev = None
                self.mru.next = Node((key, value), None, self.mru)
                self.mru = self.mru.next
            
            self.hash[key] = self.mru


# 11/19 Revisited. Well it seems I have regressed. Took way more submissions this time around. Sloppy performance all around
# Improvements: most_recent and least_recent can be dummy nodes. That helps reduce the # of cases because node.prev and node.next 
#               will never be null. Then you can abstract out methods like removeFromList() and insertIntoHead()
class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.keys = {} # key : pointer to val
        self.most_recent = None # RHS of LL
        self.least_recent = None # LHS of LL
        self.cap = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.keys:
            node = self.keys[key]
            if not node.next:
                pass # Node is most recent, do nothing
            else:
                if not node.prev: # Node is least recent, update least recent
                    self.least_recent = self.least_recent.next
                    self.least_recent.prev = None
                else: # Node is in the middle, delete from middle
                    node.prev.next = node.next
                    node.next.prev = node.prev
                
                # MTF
                self.most_recent.next = node
                node.prev = self.most_recent
                node.next = None
                self.most_recent = self.most_recent.next
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys: # update, no evict
            self.keys[key].val = value
            self.get(key) # MTF
            return
        elif self.size < self.cap: # add, no evict
            self.size += 1
        else: # add, with evict
            least_recent_key = self.least_recent.key # invariant: self.least_recent != None
            self.keys.pop(least_recent_key)
            self.least_recent = self.least_recent.next
            if self.least_recent:
                self.least_recent.prev = None
        
        # Add to front
        if self.least_recent:
            self.most_recent.next = Node(key, value, None, self.most_recent)
            self.most_recent = self.most_recent.next
        else:
            self.most_recent = Node(key, value, None, None)
            self.least_recent = self.most_recent
        
        self.keys[key] = self.most_recent
