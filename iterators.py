# Python Iterators 
# Note that for Python 3, it is items() instead of iteritems()

print "##########################"
print "1. Python array iterator"
for i in [1,2,3,4,5]:
    print i

print "##########################"
print "2. Python dict iterator"
print "--------------------------"
print "2.1 Python dict key value iterator"
for i in {"x":1,"y":2}.iteritems():
    print i
print "--------------------------"
print "2.1 Python dict key iterator"
for i in {"x":1,"y":2}.iterkeys():
    print i
print "--------------------------"
print "2.3 Python dict value iterator"
for i in {"x":1,"y":2}.itervalues():
    print i
print "--------------------------"
print "2.4 Python dict using items by default getting unordered"
a = {"x":1,"y":2, "z":3}
for i in a.items():
    print i
print list(a)
print a.keys()
print a.values()
print "--------------------------"
print "2.5 Python dict with order sequentially"
a = {"x":1,"y":2, "z":3}
print a
for d in sorted(a):
  print d
print "--------------------------"
print "2.5 Python dict of dict iterator"
d = [{"a":1,"b":2},{"a":3,"b":4}]
for i in d:
  for x in i.iteritems():
    print x

print "##########################"
print "3. Python iter built in function"
x = iter([1, 2, 3])
print x.next()
print x.next()
print x.next()
