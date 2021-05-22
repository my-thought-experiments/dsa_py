import pytest
from stack.stack import Stack

def test_push():
  stk = Stack()
  stk.push('10')
  stk.push('20')
  stk.push('30')

  assert stk.size() == 3

def test_pop():
  stk = Stack()
  stk.push('10')
  stk.push('20')
  stk.push('30')
  assert stk.size() == 3

  stk.pop()
  assert stk.size() == 2

def test_is_empty():
  stk = Stack()
  stk.push('10')
  stk.push('20')
  stk.push('30')
  assert stk.is_empty() == False

  stk.pop()
  stk.pop()
  stk.pop()
  assert stk.is_empty() == True

  try:
    stk.pop()
  except:
    assert pytest.raises(TypeError)
