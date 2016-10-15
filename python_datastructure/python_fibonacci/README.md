# Fibonacci
Fibonacci formula :
```
Fn = Fn-1 + Fn-2

Index             : 0, 1, 2, 3, 4, 5, 6, 7,  8,  9,  10, 11, 12
Fibonacci Numbers : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
```

#### 1. fibonacci using recurssion formula.
```
def fibo_recur(n):
  if n==1 or n==2:
    return 1
  return fibo_recur(n-1)+fibo_recur(n-2)
print fibo_recur(12)
```
output: 144

#### 2. fibonacci using loop.
```
def fibo(n):
  a,b = 1,1
  for i in range(n-1):
    a,b = b,a+b
    return a
print fibo(12)
```
output: 144
