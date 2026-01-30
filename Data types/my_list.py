straw_hats = ["luffy", "zoro", "nami", "usopp", "sanji"]

print(straw_hats[0])

straw_hats.append("chopper")
print(straw_hats)

straw_hats.insert(1, "robin")
print(straw_hats)

straw_hats.remove("usopp")
print(straw_hats)

straw_hats.pop()
print(straw_hats)

straw_hats.sort()
print(straw_hats)

straw_hats.sort(reverse=True)
print(straw_hats)

straw_hats2 = ["franky", "brook", "jinbe"]
all_straw_hats = straw_hats + straw_hats2
print(all_straw_hats)

print(len(all_straw_hats))
print(all_straw_hats.index("nami"))
print(all_straw_hats.count("luffy"))
all_straw_hats.reverse()
print(all_straw_hats)

for member in all_straw_hats:
    print(member)
    
straw_hats_copy = all_straw_hats.copy()
print(straw_hats_copy)

straw_hats[1:3] = ["robin", "zoro"]
print(straw_hats)

del straw_hats[0]
print(straw_hats)

straw_hats.clear()
print(straw_hats)

#list comprehension
squares = [x**2 for x in range(10)]
print(squares)

even_squares = [x**2 for x in range(10) if x%2==0]
print(even_squares)

