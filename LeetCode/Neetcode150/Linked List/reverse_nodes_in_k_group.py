# thoughts
# - the recursive step for this algorithm is tough to get right
#   - a bad algorithm (like mine) has edge cases, so you need if statements to resolve them
#   - in this case though, i like the bad algorithm better because the good algorithm feels hacky too
# - remember that when you modify a linked list in place, dummy still picks up on all of these changes

# initial - messy solution but it passes and I think time/space are good
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l, r = head, head
        for i in range(k-1):
            if not r:
                break
            r = r.next
        cur = head
        dummy = None

        while l:
            for i in range(k-1):
                if l:
                    l = l.next
                if r:
                    r = r.next
            if l:
                l = l.next
            else:
                break
            if r:
                r = r.next

            prev = r if r else l
            for i in range(k):
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            if not dummy:
                dummy = ListNode(0, prev)

        return dummy.next if dummy else head

# Neetcode solution is simpler in that it has less if conditions, but imo less understandable because of pointer bullshit
# Some annotations using example head = 1->2->3->4->5-> and k = 2
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        groupPrev = dummy # the node 1 before the current group

        while True:
            kth = self.getKth(groupPrev, k) # the last node in the current group (before reversal)
            if not kth:
                break
            groupNext = kth.next # the node 1 after the current group

            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            # at this point: 2->1->3->4->5->
            #                   ^
            #                   |
            #                 dummy

            tmp = groupPrev.next
            groupPrev.next = kth
            # at this point: 2->1->3->4->5->
            #                ^
            #                |
            #              dummy
            # groupPrev is an alias of dummy, and this change mutates the object that both groupPrev and dummy are pointing to, rather than assigning a new value to groupPrev
            # In later iterations, groupPrev no longer is an alias, but continues to modify the same linked list, so that dummy is "picking up" all the changes
            groupPrev = tmp
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr