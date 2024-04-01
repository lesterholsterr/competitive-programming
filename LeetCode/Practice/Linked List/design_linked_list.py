class Node:
  def __init__(self, val, next):
      self.val = val
      self.next = next

class MyLinkedList(object):
  def __init__(self):
      self.head = None
      
  def get(self, index):
      """
      :type index: int
      :rtype: int
      """
      if self.head is None:
          return -1
      itr = self.head
      count = 0
      while count < index:
          itr = itr.next
          count += 1
          if itr is None:
              return -1
              break
      return itr.val
      

  def addAtHead(self, val):
      """
      :type val: int
      :rtype: None
      """
      self.head = Node(val, self.head)
      

  def addAtTail(self, val):
      """
      :type val: int
      :rtype: None
      """
      itr = self.head
      if itr is None:
          self.head = Node(val, None)
          return
      while itr.next:
          itr = itr.next
      itr.next = Node(val, None)
      

  def addAtIndex(self, index, val):
      """
      :type index: int
      :type val: int
      :rtype: None
      """
      itr = self.head
      count = 0
      if index == 0:
          self.addAtHead(val)
          return
      while count+1 < index:
          itr = itr.next
          count += 1
          if itr is None:
              return
      itr.next = Node(val, itr.next)
      

  def deleteAtIndex(self, index):
      """
      :type index: int
      :rtype: None
      """
      itr = self.head
      count = 0
      if index == 0:
          self.head = self.head.next
          return
      while count+1 < index:
          itr = itr.next
          count += 1
          if itr is None:
              return
      if itr.next is None:
          return
      elif itr.next.next is None:
          itr.next = None
      else: itr.next = itr.next.next
  
  
  def print(self):
    if self.head is None:
      print("Linked list is empty")
      return
    
    itr = self.head
    llstr = ''
    while itr:
      llstr += str(itr.val) + '-->'
      itr = itr.next
    print(llstr)