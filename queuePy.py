class Queue:
  def __init__(self):
    self.data = []

  def insert(self, x):
    self.data.append(x)
  
  def empty(self):
    return not len(self.data) > 0

  def remove(self):
    if not self.empty():
      return self.data.pop(0)

q = Queue()
q.insert(1)
q.insert(2)
q.insert(3)

while not q.empty():
  print(q.remove())
