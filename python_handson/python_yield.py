def yield_fun(a):
  print "start"
  for i in range(a):
    print "i before yield", i
    yield i
    print "i after yield", i
  print "end"

obj = yield_fun(4)
obj.next()
obj.next()
obj.next()
obj.next()
obj.next()  # on this line you will get the StopIteration error
