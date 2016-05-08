# Python sets operations
# this is the set 
a = {1,1,12,2,2,2,3,4,5,6,8,"asd","df","asd"}
# or a = set()
print a
b = {1,5,6,7,7,8,9,12,"df"}
print b

# laters in a but not in b
c = a - b
print c

# laters in b but not in a
c = b - a
print c

# laters in either a or b  (a union b)
c = a | b
print c

# laters common in a and  b  (a intersection b)
c = a & b
print c

# laters in a or  b but not both (a  b)
c = a ^ b
print c

# sets comprehensions
a = {x for x in 'abracadabra' if x not in 'abc'}
print a
