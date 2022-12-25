class Node:
  def __init__(self, val, next, prev):
      self.val = val
      self.next = next
      self.prev = prev

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
      return itr.val
      

  def addAtHead(self, val):
      """
      :type val: int
      :rtype: None
      """
      self.head = Node(val, self.head, None)
      

  def addAtTail(self, val):
      """
      :type val: int
      :rtype: None
      """
      itr = self.head
      if itr is None:
          self.head = Node(val, None, None)
          return
      while itr.next:
          itr = itr.next
      itr.next = Node(val, None, itr)
      

  def addAtIndex(self, index, val):
      """
      :type index: int
      :type val: int
      :rtype: None
      """
      if index == 0:
          self.addAtHead(val)
          return

      itr = self.head
      if itr is None:
          return
      count = 1
      while count < index:
          itr = itr.next
          count += 1
          if itr is None:
              return
      
      new_node = Node(val, itr.next, itr)
      itr.next = new_node
      if itr.next: itr.next.prev = new_node
      
      

  def deleteAtIndex(self, index):
      """
      :type index: int
      :rtype: None
      """
      if index == 0:
          self.head = self.head.next
          if self.head: self.head.prev = None
          return
      
      itr = self.head
      count = 1
      while count < index:
          itr = itr.next
          count += 1
          if itr is None:
              return
      if itr.next is None:
          return
      elif itr.next.next is None:
          itr.next = None
      else:
          itr.next = itr.next.next
          itr.next.prev = itr
  
  
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

ll = MyLinkedList()
ll.addAtIndex(2, 0)
ll.get(0)
ll.print()