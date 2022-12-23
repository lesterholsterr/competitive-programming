class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution(object):
  def isPalindrome(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head is None: return True
    if head.next is None: return False

    first = head.val
    itr = head.next
    if itr.next is None: return True if first == itr.val else False
    while itr.next.next:
      itr = itr.next
    last = itr.next.val
    itr.next = None

    if first == last:
      self.isPalindrome(itr)
    else: return False