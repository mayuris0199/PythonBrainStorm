# iterators
#for i in range(1):
#  print i

# The built-in function iter takes an iterable object and returns an iterator.
x = iter([1, 2, 3])
#print x.next()
#print x.next()
#print x.next()

def f(n):
  return [x**3 for x in range(n)]

def g(n):
  for i in range(n):
    yield i**3

# Example 2
import itertools
#iteratior
A = [x for x in itertools.permutations('123')]
print A

# Generator
B = (x for x in itertools.permutations('123'))
while True:
  try:
    print B.next()
  except :
    break
