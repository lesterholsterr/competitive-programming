# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Solution 1: 2 Iterations
        if head.next is None:
            return None

        l = 0
        itr = head
        while itr:
            itr = itr.next
            l += 1
        
        target = l - n - 1
        if target == -1:
            return head.next

        itr = head
        for i in range(target):
            itr = itr.next
        itr.next = itr.next.next
        return head

        # Solution 2: 2 Pointer
        if head.next is None:
            return None
        
        left = head
        right = head
        for i in range(n):
            right = right.next
        if right is None:
            return head.next
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return head