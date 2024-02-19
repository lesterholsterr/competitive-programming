# Overall: I mean this was just an annoying problem what did I even learn

# Initial Solution
# Not entirely sure why but division seems to break when the numbers are too big
# Welp I'm sure this was not the intended solution anyways because other languages
# don't support ints of infinite size...
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        n1, n2 = 0, 0

        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        while s1:
            n1 += s1.pop()
            if len(s1) > 0:
                n1 *= 10
        while s2:
            n2 += s2.pop()
            if len(s2) > 0:
                n2 *= 10
        
        n1 += n2
        if n1 == 0:
            return ListNode()
        
        ans = ListNode()
        cur = ans
        while n1 != 0:
            d = n1 % 10
            cur.next = ListNode(d)
            cur = cur.next
            n1 = int((n1 - d) / 10)
        
        return ans.next
    
# Second Solution
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        cur = ans
        carry = 0

        while l1 or l2 or carry != 0:
            d = 0
            if l1:
                d += l1.val
                l1 = l1.next
            if l2:
                d += l2.val
                l2 = l2.next
            if carry != 0:
                d += carry
                carry = 0
            
            if d <= 9:
                cur.next = ListNode(d)
            else:
                cur.next = ListNode(d % 10)
                carry = 1
            cur = cur.next
        
        return ans.next