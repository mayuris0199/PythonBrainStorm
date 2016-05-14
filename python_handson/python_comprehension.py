# simple way to make list
a = []
for i in range(10):
  a.append(i*2)
print a
 
# list comprehension 
a = [i*2 for i in range(10)]
print a

# simple way to make dict
a = {}
for i in range(10):
  a[i] = i*2
print a

# dict comprehension
a = {i:i*2 for i in range(10)}
print a
