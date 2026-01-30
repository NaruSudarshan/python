# decorators are higher order functions which take function as argument and return a modified function
# basicaly do something before and after the function call

# baasic structure of decorator
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        # do something before
        result = original_function(*args, **kwargs)
        # do something after
        return result
    return wrapper_function

import time 

# this is a decorator function
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} ran in {end_time - start_time} seconds")
        return result
    return wrapper

# using the decorator
# example_function is sent as argument to timer and the modified function wrapper is returned 
# and whenever example_function is called , wrapper is executed
@timer
def example_function(n):
    time.sleep(n)
    return f"Slept for {n} seconds"

# print(example_function(2))  # without decorator

print(example_function(3))  # with decorator



