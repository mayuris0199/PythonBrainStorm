# Generators
#Generators are iterators, but you can only iterate over them once. It's because they do not store all the values in memory, they generate the values on the fly, It is just the same except you used () instead of []

a = (x*x for x in range(3))
print a

for i in a:
  print i
 
# Yield keyword 

def abc(val):
  for i in val:
    yield i 

val = range(10)
abc(val)    
