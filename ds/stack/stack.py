class Stack:
  def __init__(self):
    self.elements = []

  def push(self, element):
    self.elements.append(element)

  def pop(self):
    if self.is_empty() == True:
      raise Exception("Stack is empty, nothing to pop")
    self.elements.pop()

  def is_empty(self):
    if self.size() == 0:
      return True
    return False

  def size(self):
    return len(self.elements)
