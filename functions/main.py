# example of **kwargs , kwargs is dictionary
def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        example_function(name="Alice", age=30, city="New York")

# example of *args , args is tuple
def sum_all(*args):
    return sum(args)
result = sum_all(1, 2, 3, 4, 5)

#example of lambda function
square = lambda x: x * x
print(square(6))  

# named arguments
def greet(name, message="Hello"):
    print(f"{message}, {name}!")
    
#keyword arguments
greet(message="Hi", name="Bob")
greet("Charlie")  # uses default message

# default arguments
greet("Diana", "Welcome")

# function with yeield 
# yield is used to create generator functions 
# this is stateful function , it remembers its state between calls
# for example in this function , it remembers the last value of i and next time when next() is called , it starts from there
# python takes care of memory management here
def even_generator(n):
    for i in range(2, n + 1, 2):
        yield i
        
for even in even_generator(20):
    print(even)


# recrusive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5)) 