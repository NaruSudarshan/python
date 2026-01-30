dict = {}

arr = ["a", "b", "c", "d", "e","a", "b"]

for i in arr:
    dict[i] = dict.get(i,0) + 1
    
print(dict["a"])

for key in dict:
    print(f"{key} : {dict[key]}",end = ",")
    
print()
    
for key ,value in dict.items():
    print(f"{key} : {value}",end =",")
    
print()

print(dict)

# sorting 
sorted_dict = dict(sorted(dict.items()))
print(sorted_dict)

reverse_sorted_dict = dict(sorted(dict.items(), reverse=True))
print(reverse_sorted_dict)

sort_with_values  = dict(sorted(dict.items(),key = lambda x : x[1]))
print(sort_with_values)

sort_with_values_then_keys  = dict(sorted(dict.items(),key = lambda x : (x[1],x[0])))
print(sort_with_values_then_keys)

sort_with_reverse_values_then_keys  = dict(sorted(dict.items(),key = lambda x : (-x[1],x[0])))
print(sort_with_reverse_values_then_keys)

# dictionary comprehension
squared_dict = {x: x**2 for x in range(6)}
print(squared_dict)

even_squared_dict = {x: x**2 for x in range(6) if x%2==0}
print(even_squared_dict)