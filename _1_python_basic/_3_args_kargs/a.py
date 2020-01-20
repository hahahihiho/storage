# *args pass a variable number of arguments to a function.
# **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list.

def add_many(*args): 
    result = 0
    for i in args: 
        result = result + i 
    print(result)

onetofive=[1,2,3,4,5]
add_many(*onetofive)
add_many(1,2,3,4,5)

def myFun0(**kwargs):  
    print(kwargs)
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
myFun0(first ='Geeks', mid ='for', last='Geeks')

def myFun(arg1, arg2, arg3): 
    print("arg1:", arg1) 
    print("arg2:", arg2) 
    print("arg3:", arg3) 
      
# Now we can use *args or **kwargs to 
# pass arguments to this function :  
args = ("Geeks", "for", "Geeks") 
myFun(*args) 
  
kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"} 
myFun(**kwargs) 
