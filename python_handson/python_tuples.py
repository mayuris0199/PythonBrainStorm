#A tuple is a sequence of immutable Python objects
tup1 = ("sd",23,"3",233,"rr")
tup2 = ("sd22",2,"r")

# add tuples
t = tup1 + tup2
print t

# access tuple with indexed
print tup1[4]

# you can not update tuples because its immutable
tup1[4] = 122
#TypeError: 'tuple' object does not support item assignment

# Deleting tuple
del tup1

#check length of tuple
len(tup1)
