# Definition for singly-linked list.
class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Overall: In Python, next is another Node, while in C++ it is a pointer. So assigning x = node.next, where node.next = None, and then reassigning x = Node(val=5) does not change node.next!

        # Initial Attempt (15 minutes)
        # This problem is super easy. I think I still have some fundamental misunderstanding of how linked lists work in Python, and so wasn't able to solve it :(
        cur1 = list1 
        cur2 = list2 # <-- this is unnecessary. list1 and list2 are nodes too. There is no need to keep the heads of the lists, so we can just traverse using list1 and list2.
        sorted = Node()
        cur = sorted.next # <-- should be equal to the dummy node, not its next pointer. sorted.next is None, so all we did was assign cur to None, then reassign it to a node later. In C, sorted.next would be a pointer, so something like this might actually work. In Python, we let cur = sorted, and in the while loop, create a Node and assign it to cur.next in one line.

        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur = Node(val=cur1.val)
                cur = cur.next
                cur1 = cur1.next
            else:
                cur = Node(val=cur2.val)
                cur = cur.next
                cur2 = cur2.next

        if cur1:
            cur = cur1
        elif cur2:
            cur = cur2
        return sorted.next

        # Neetcode Solution
        dummy = Node()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = Node(val=list1.val)
                list1 = list1.next
            else:
                tail.next = Node(val=list2.val)
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next