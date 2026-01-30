straw_hats = ("luffy", "zoro", "nami", "usopp", "sanji")
print(straw_hats[0])
print(len(straw_hats))
# straw_hats[0] = "chopper" # error -> tuples are immutable
for member in straw_hats:
    print(member)

# single element tuple
single_element_tuple = ("only_one",)
print(type(single_element_tuple))
not_a_tuple = ("only_one")
print(type(not_a_tuple))  
  
# tuple unpacking
a, b, c, d, e = straw_hats
print(a)

x, y, *rest = straw_hats
print(rest)