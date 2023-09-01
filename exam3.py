from node import Node

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0
    
  def enqueue(self, value):
    item_to_add = Node(value)

    # Add code below
    
         
  def dequeue(self):
    if self.is_empty():
      return None

    item_to_remove = self.head
    if self.get_size() == 1:
      self.head = None
      self.tail = None
    else:
      self.head = self.head.get_next_node()
    self.size -= 1

    return item_to_remove.get_value()
  
  def peek(self):
    if self.is_empty():
      return None
    
    return self.head.get_value()
    
  def get_size(self):
    return self.size
    
  def is_empty(self):
    return self.size == 0
  
q = Queue()
print("Enqueue value: 1")
q.enqueue(1)
print("Output of peek: " + str(q.peek()))
print("Enqueue value: 2")
q.enqueue(2)
print("Output of peek: " + str(q.peek()))