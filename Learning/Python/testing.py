class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k: int):
    dummy = ListNode(0, head)
    groupPrev = dummy # the node 1 before the current group

    while True:
        kth = getKth(groupPrev, k) # the last node in the current group (before reversal)
        if not kth:
            break
        groupNext = kth.next # the node 1 after the current group

        prev, curr = kth.next, groupPrev.next
        while curr != groupNext:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # at this point: 2->1->3->4->5-> and dummy->1->3->4->5-> 

        tmp = groupPrev.next
        groupPrev.next = kth 
        # at this point: dummy->2->1->3->4->5
        # we are modifying the provided linked list in place, so dummy is "picking up" all these changes!
        groupPrev = tmp
        
    return dummy.next

def getKth(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr

ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
ll2 = reverseKGroup(ll, 2)

cur = ll2
while cur:
    print(cur.val, "->", sep='', end='')
    cur = cur.next
