class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    n1, n2 = 0, 0

    while l1:
        n1 += l1.pop()
        if len(l1) > 0:
            n1 *= 10
    while l2:
        n2 += l2.pop()
        if len(l2) > 0:
            n2 *= 10
    return n1 + n2
    # n1 += n2
    # ans = []
    # while n1 != 0:
    #     ans.append(n1 % 10)
    #     n1 = int((n1 - n1 % 10) / 10)
    
    return ans

# x = 1000000000000000000000000000466
# print(x)
# while x != 0:
#     print(x % 10)
#     x = (x - x%10) / 10
#     print(x)

# print(addTwoNumbers([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [5,6,4]))

print(int(2**0.5))