class Node:
  # A Node is a (data pointer)
  #   data is anything
  #   pointer is one of: None, Node
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

class LinkedList:
  # A LinkedList is a Node
  # Initialized as None, an empty LinkedList
  def __init__(self):
    self.head = None
  
  # new_node is a Node with the desired data that points to the existing LinkedList
  def insert_at_beginning(self, data):
    new_node = Node(data, self.head)
    self.head = new_node
  
  # is None (?)
  # while itr (?)
  def print(self):
    if self.head is None:
      print("Linked list is empty")
      return
    
    itr = self.head
    llstr = ''
    while itr:
      llstr += str(itr.data) + '-->'
      itr = itr.next
    print(llstr)
  
  def append(self, data):
    if self.head is None:
      self.head = Node(data, None)
      return
    
    itr = self.head
    # Continue iterating until the pointer is empty
    while itr.next:
      itr = itr.next
    itr.next = Node(data, None)

  def insert_values(self, data_list):
    self.head = None
    for elem in data_list:
      self.append(elem)
    # return ll
  
  def length(self):
    itr = self.head
    length = 0
    while itr:
      itr = itr.next
      length += 1
    return length
  
  def remove_at(self, at):
    if at < 0 or at >= self.length():
      raise Exception("Invalid Index")
    
    if at == 0:
      self.head = self.head.next
      return

    itr = self.head
    count = 0
    while itr:
      if count == at-1:
        itr.next = itr.next.next
        break
      itr = itr.next
      count += 1
  
  def insert_at(self, data, at):
    if at < 0 or at >= self.length():
      raise Exception("Invalid Index")
    
    if at == 0:
      self.head = Node(data, self.head)
      return
    
    itr = self.head
    count = 0
    while itr:
      if count == at-1:
        itr.next = Node(data, itr.next)
        break
      itr = itr.next
      count += 1
  
  def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
    if self.head is None:
      return
    
    itr = self.head
    while itr:
      if itr.data == data_after:
        itr.next = Node(data_to_insert, itr.next)
        break
      itr = itr.next


  def remove_by_value(self, data):
      # Remove first node that contains data
      if self.head is None:
        return
      
      if self.head.data == data:
        self.head = self.head.next
        return

      itr = self.head
      while itr.next:
        if itr.next.data == data:
          itr.next = itr.next.next
          break
        itr = itr.next
  
  def isPalindrome(self):
    """
    :type head: ListNode
    :rtype: bool
    """
    if self.head is None: return True
    if self.head.next is None: return False

    first = self.head.data
    itr = self.head.next
    if itr.next is None:
      if first == itr.data:
        print("yep")
        return True
      else: return False
    while itr.next.next:
      itr = itr.next
    last = itr.next.data

    if first == last:
      self.remove_at(self.length()-1)
      self.remove_at(0)
      self.isPalindrome()
    else: return False

if __name__ == '__main__':
  ll = LinkedList()
  ll.insert_values([1, 2, 3, 3, 2, 1])
  ll.print()
  if ll.isPalindrome(): print("Palindrome")
  # ll.insert_values(["banana","mango","grapes","orange"])
  # ll.print()
  # ll.insert_after_value("mango","apple") # insert apple after mango
  # ll.print()
  # ll.remove_by_value("orange") # remove orange from linked list
  # ll.print()
  # ll.remove_by_value("figs")
  # ll.print()
  # ll.remove_by_value("banana")
  # ll.remove_by_value("mango")
  # ll.remove_by_value("apple")
  # ll.remove_by_value("grapes")
  # ll.print()