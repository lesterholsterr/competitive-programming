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
        # Solution 1: Iterative
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        merged = cur = Node()
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1 != None:
            cur.next = list1
        else: 
            cur.next = list2
        return merged.next

        # Solution 2: Recursive
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2