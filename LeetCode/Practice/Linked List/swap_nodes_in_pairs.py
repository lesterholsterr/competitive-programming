# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        elif head.next is None:
            return head
        else:
            a, b = head, head.next
            prev, dummy = ListNode(0, b), ListNode(0, b.next)
            b.next, a.next = a, self.swapPairs(dummy.next)
        return prev.next