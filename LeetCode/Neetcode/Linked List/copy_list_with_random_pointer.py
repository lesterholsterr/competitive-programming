"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        # Overall: Quantify your requirements and see what data structures fit them!
        # Leaps
        # - A deep copy of the val and next pointers can be done in one pass. How can we make a copy of the random nodes also in linear time?
        # - Given a random node from the original list, I want to find out what the corresponding node is in the new list. What data structure can do this?

        # Initial Attempt (20 minutes)
        if head is None:
            return None

        dummy = Node(0)
        old = head
        new = Node(old.val)
        dummy.next = new
        old = old.next

        while old:
            new2 = Node(old.val)
            new.next = new2
            new = new2
            old = old.next

        # Second Solution (with hint)
        if head is None:
            return None

        dummy = Node(0)
        nodes = {}

        old = head
        new = Node(old.val)
        dummy.next = new
        nodes[old] = new
        old = old.next

        while old:
            temp = Node(old.val)
            new.next = temp
            new = temp
            nodes[old] = new
            old = old.next

        old = head
        new = dummy.next
        while old:
            if old.random is None:
                new.random = None
            else:
                new.random = nodes[old.random]
            old = old.next
            new = new.next

        return dummy.next

        # Neetcode Solution
        # Mapping null to null so we don't have to manually check for null pointers in the second while loop
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]  # BIG BRAIN WAY TO NOT USE DUMMY NODE
