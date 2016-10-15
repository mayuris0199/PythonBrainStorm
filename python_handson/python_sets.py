# Python sets operations
#1. this is the set 
a = {1,1,12,2,2,2,3,4,5,6,8,"asd","df","asd"}
# or a = set()
print a
b = {1,5,6,7,7,8,9,12,"df"}
print b

#2. laters in a but not in b
c = a - b
print c

#3. laters in b but not in a
c = b - a
print c

#4. a.union(b) - Returns a new set with all elements from both sets
# laters in either a or b  (a union b)
c = a | b
print ("union",c)

#5. a.intersection(b) - Returns a new set with only those elements common to both sets 
#laters common in a and  b  (a intersection b)
c = a & b
print ("intersection",c)

#6. a.difference(b) - Returns a new set with all items from first set not in second 
#laters in a or  b but not both (a  b)
c = a ^ b
print ("diffrence", c)

#7. a.issubset(b) - Asks whether all elements of one set are in the other then true else false
c = a.issubset(b)
print ("subset",c)

#8. a.add(item) - Adds item to the set
c = a.add("323")
print (a)
print ("add", c)

#9. a.remove(item) - Removes item from the set
c = a.remove("df")
print (a)
print ("remove", c)

#10. a.pop() - Removes an arbitrary element from the set
c = a.pop()
print a
print c

#11. a.clear() - Removes all elements from the set
a.clear()
print a

#12. sets comprehensions
a = {x for x in 'abracadabra' if x not in 'abc'}
print a
