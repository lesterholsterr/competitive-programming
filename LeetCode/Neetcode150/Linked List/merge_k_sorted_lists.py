# Overall: Not sure why this question is labelled hard...
# Good way of thinking about problems that might be reducible to known problems
# - Pretend you have a solver for the known problem. Is there an algorithm to
#   put these smaller solutions together? In this case it is merge sort.

# Initial Solution
# Time: O(nlogn) (where n = # of nodes)
# Wonder if linear is possible
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = ListNode()
        cur = ans
        freq = {}

        for ll in lists:
            while ll:
                if ll.val in freq:
                    freq[ll.val] += 1
                else:
                    freq[ll.val] = 1
                ll = ll.next

        if len(freq) == 0:
            return None

        keys = sorted(freq.keys())
        for k in keys:
            for i in range(freq[k]):
                cur.next = ListNode(k)
                cur = cur.next

        return ans.next

# Neetcode Solution
# Time: O(nlogk)
# Merge sort + merge 2 lists. Definitely should review sorting. Would not have found this myself.


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def m2(l1, l2):
            ans = ListNode()
            cur = ans
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    cur.next = ListNode(l2.val)
                    l2 = l2.next
                cur = cur.next  # forgot this step smh
            if not l1:
                cur.next = l2
            else:
                cur.next = l1
            return ans.next

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(m2(l1, l2))
            lists = mergedLists

        return lists[0]
