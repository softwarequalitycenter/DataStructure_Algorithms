class MaxStack:
  def __init__(self):
    self.stack = []

  def push(self, val):
    self.stack.append(val)

  def popp(self):
     l = len(self.stack)
     if l <=0 :
         return -1
     popped= self.stack[l-1]
     del self.stack[l-1]
     return popped

  def max(self):
      max = 0
      a = self.popp()
      while self.popp() != -1:
          if max < a :
              max = a
      return max


s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print (s.max())
# 3

s.popp()
s.popp()
print (s.max())
# 2
