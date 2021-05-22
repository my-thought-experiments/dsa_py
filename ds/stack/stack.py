class Stack:
  def __init__(self):
    self.elements = []
    self.count = 0

  def push(self, element):
    self.elements.append(element)

  def pop(self):
    if (self.is_empty()):
      return 'Stack is empty, nothing to pop'
    self.elements.pop()

  def is_empty(self):
    return self.elements == 0

  def size(self):
    return len(self.elements)
