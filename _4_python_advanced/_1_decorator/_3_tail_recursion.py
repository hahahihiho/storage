# tail_recursion.py
class Recurse(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

def recurse(*args, **kwargs):
    raise Recurse(*args, **kwargs)
        
def tail_recursive(f):
    def decorated(*args, **kwargs):
        while True:
            try:
                return f(*args, **kwargs)
            except Recurse as r:
                args = r.args
                kwargs = r.kwargs
                continue
    return decorated
    
@tail_recursive
def factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    recurse(n-1, accumulator=accumulator*n)

def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)

# tail recursion(stack overflow x)
print(factorial(1000))
# recursion(stack overflow)
print(fac(999))
