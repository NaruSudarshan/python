f = open("example_file.py")

# here f is same as iter(list) for the list , no need to do iter(f) again (this is only for files)

line_1 = f.readline() # sends next
line_2 = f.readline()
line_3 = f.readline()
line_4 = f.readline()
line_5 = f.readline() # ""
line_6 = f.readline() # ""

print(line_1,line_2,line_3,line_4) 
print(f" line 5 , 6 are {line_5}{line_6} !!!")

# working of __next__ 
# f2 = open("example_file.py")
# print(f2.__next__())
# print(f2.__next__())
# print(f2.__next__())
# print(f2.__next__())
# print(f2.__next__())
# print(f2.__next__())

# using for loop
f3 = open("example_file.py")
for line in f3:
    print(line)
    
# iterating lists internally 

my_list = [10,20,30,40,50]
I = iter(my_list)
print(I)
print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())
# print(I.__next__()) # StopIteration


