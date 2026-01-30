name = "Naru Sudarshan"

first_char = name[0]
print(first_char)

first_name = name[0:4]
print(first_name)

statement = "my name is {}"
print(statement.format(name))

name_list = name.split()
print(name_list)

name_from_list = " ".join(name_list)
print(name_from_list)

he_said = "hello \"how are you ? \" "
print(he_said)

#raw string -> everything is treated as string without formating 
path = r"c:\user\pwd"
# path = "c:\\user\\pwd" this is same as above
print(path)