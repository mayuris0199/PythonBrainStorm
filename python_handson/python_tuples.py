#A tuple is a sequence of immutable Python objects
# Create tuples
tup1 = ("sd",23,"3",233,"rr")
tup2 = ("sd22",2,"r")
tup3 = ("sd22",2,"r")
l1 = [1 ,3, 54, 6, 5]
# add tuples
t = tup1 + tup2

print "tup1",tup1
print "tup2",tup2
print "tup3",tup3

# access tuple with indexed
print tup1[4]

# you can not update tuples because its immutable
#tup1[4] = 122
#TypeError: 'tuple' object does not support item assignment

# Deleting tuple
del tup3
#Print tup3 will give and error

# built in tuple functions

#check length of tuple Gives the total length of the tuple.
print len(tup1)
#compare two tuples
print cmp(tup1, tup2)
# Returns item from the tuple with max value.
print max(tup1)
# Returns item from the tuple with min value.
print min(tup1)
#convert a list into tuples
print tuple(l1)
