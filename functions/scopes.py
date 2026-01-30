username = "chaiaurcode"

def func():
    username = "chai"
    print(username) # prints local variable chai

print(username) # prints global variable chaiaurcode
func()


x = 99 
# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)

# def func3():
#     global x
#     x = 12
    
# func3()
# print(x)

def f1():
    x = 88
    def f2():
        print(x) 
    f2() 
f1() # prints 88 because when f2 is called , it has access to f1's scope


# closure example -> when innner function remembers the outer function's scope even after the outer function has finished executing
def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1() # we are storing the inner function f2 and its scope (x=88) in myResult
myResult() # now when we call myResult , it prints 88 because f2 has access to f1's scope even after f1 has finished executing

# example of closure with arguments
def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2) # f saves the inner function actual with num = 2
g = chaicoder(3) # g saves the inner function actual with num = 3

print(f(3))
print(g(3))