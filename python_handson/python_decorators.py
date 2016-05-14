def deco(fn):
  # this will only run when decorator call with @deco
  print("start with decorator")

  def deco_inside():
    print("You are calling function %s with @deco from function deco_inside" % (fn.__name__))
    #from decorator you can call functions which are outside decorator
    fn()
    print ("completed function %s" % (fn.__name__))
  return deco_inside

@deco
def new_func():
  print("run this function from decorator")

new_func()
 
# output 
"""
start with decorator
You are calling function new_func with @deco from function deco_inside
run this function from decorator
completed function new_func
"""
