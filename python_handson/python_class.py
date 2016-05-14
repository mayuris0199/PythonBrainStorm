# python class
class a:
  def __init__(self,x,y):
    self.x = x
    self.y = y

  def b(self):
    print self.x

if __name__ == "main":
  c = a("hello", "world")
  print a.b()
  print c.b()
