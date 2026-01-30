# decorator to cache function results (memoization) n return the cached result if the function is called with same arguments again

import time 

def cache_decorator(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
        return result
    return wrapper

@cache_decorator
def long_running_function(a,b):
    time.sleep(5)
    return a+b

print(long_running_function(2,3)) # takes 5 secs 
print(long_running_function(2,3)) # takes <5 because cached 
print(long_running_function(2,5)) # takes 5 seconds 