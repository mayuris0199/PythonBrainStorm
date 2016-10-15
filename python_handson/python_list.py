# Python list 
# initialize empty python list
a = []
print a

# append items in python list
a.append(1)
a.append(2)
a.append(3)
a.append(12)
a.append(13)
a.append(3)
a.append(4)
print a

# 1. Insert items in list 
a.insert(len(a),2)
print a

# 2. remove items from list
a.remove(12)
print a

# 3. pop items from last of list 
a.pop()
print a

# 4. check index of values  
print a.index(13)

# 5. count no of values in list
print a.count(3)

# 6. count the total value in list
print len(a)

# 7. sort the list
print sorted(a)

# 8. reverse the list
print list(reversed(a))
print a[::-1]

# 9. access list by index
print a[2:4]

# 10. list comprehensions
squares = [x**2 for x in range(10)]
print squares
