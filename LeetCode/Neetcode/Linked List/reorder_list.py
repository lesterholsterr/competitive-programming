# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        # Overview: Probably could not have come up with the constant memory solution myself, but pretty good overall
        # Leaps
        # - Realize that this problem is straightforward if we had 2 lists: the first half, and the reversed second half
        # - Always check where the final head and tail are pointing to avoid cycles

        # Initial Solution (20 minutes)
        # O(n) time and memory. We can probably do constant memory and a less scrappy solution...
        l = 0
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
            l += 1

        index = 0
        x = 1
        for i in range(l-1, 0, -1): # had to look up the syntax for descending range lol
            nodes[index].next = nodes[index + i*x]
            index += i*x
            x *= -1
            # Failed to consider this and initally ended up with a cycle in the linked list
            if i == 1:
                nodes[index].next = None
    
        # Neetcode Solution
        # Find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half
        second = slow.next
        slow.next = None # Don't forget this, otherwise you create a cycle again!!!
        prev = None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next
        
        # Merge 2 halves
        first = head
        second = prev # Important to keep track of the "end state" of second and prev once the reversal is completed
        # Since we started fast at head.next, we know the 2nd half of the list will always be equal length or shorter, so no need to check the first half
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1 # At first I thought first should be assigned to temp1.next. Can you convince yourself why that would be wrong now?
            second = temp2