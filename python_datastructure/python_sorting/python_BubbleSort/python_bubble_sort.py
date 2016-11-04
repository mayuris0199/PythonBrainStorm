#Bubble Sort Algorithm
import sys
def bubble_sort(l):
#l =  [n for n in l for i in xrange(len(l)) ]
  print l
  a = None
  b = None
  for i in l:
    if a == None:
      a = i
      continue
    b = i
    if a > b:
      ind = l.index(a)
      l[ind] = b
      l[ind+1] = a
    print l

def bubble_sorts(items):
    print items
    for i in range(len(items)):
    	    print i
            for j in range(len(items)-1-i):
	    		print j
			sys.exit(0)
	                if items[j] > items[j+1]:
			                items[j], items[j+1] = items[j+1], items[j]
    print items
#a = [9,3,7,2,8,6,5] 
#bubble_sort(a)
a = [9,3,7,2,8,6,5] 
bubble_sorts(a)
