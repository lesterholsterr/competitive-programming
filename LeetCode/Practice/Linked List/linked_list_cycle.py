# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        if head == head.next:
            return True
        slow = head
        fast = head.next
        while slow != fast:
            if slow.next is None or fast.next is None or fast.next.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True