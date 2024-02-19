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

        # Overall: Seemed like a pretty intuitive application of 2 runners, didn't have any problems with this one. Use l and r for the variable names next time though.
        # Leaps
        # - How do we solve the edge case where n = # of nodes?

        # Initial Solution (10 minutes)
        first, second = head, head
        for i in range(n):
            first = first.next
        if first is None:
            return head.next
        while first.next != None:
            first, second = first.next, second.next
        second.next = second.next.next
        return head
