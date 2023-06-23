# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # Overall: Wow this is embarassing...
        # Leaps
        # - It's clear we need 2 contiguous pointers to reverse each connection
        # - Reversing breaks the link to the next node, how do we save this?

        # Initial Attempt (20 mins)
        # Couldn't seem to figure out how to save the "next" node without affecting it when we make cur.next point to prev.
        cur = head
        prev = None
        next = cur.next
        while cur:
            cur.next = prev
            prev = cur
            cur = next

        # Neetcode Solution
        cur = head
        prev = None
        while cur:
            # <-- I SWEAR I tried this already and it didn't work...
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev  # Oh I think I just forgot to return prev >:(

        # Recursive Solution
        # Base case
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            # head.next.next should be pointing at nothing once the recursive calls return to the current stack frame
            head.next.next = head
        head.next = None

        return newHead
