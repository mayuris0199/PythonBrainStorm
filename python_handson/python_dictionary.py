# Python Disctionary operations
# this is the initialization of empty python dictionary
a = {}
print a
# add some ky values in thr dict 
a["k1"] = "v1"
a["k2"] = "v2"
a["k3"] = "v3"
# seq list of keys from dict
print sorted(a)
print a
# delete k3 key:value by key 
del a["k3"]
print a
# get the list of keys:values 
print a.items()
# get the list of keys only
print a.keys()
# get the list of values only
print a.values()
# dict comprehensions
c = {y: x**2 for x,y in enumerate(["l", "y", "z"])}
print c
# get the value of key k1 
print a["k1"]
