#creating a tuple
colour=("red","yellow","green","black")

#creating a single item as a tuple
# fruit=("apple",)
# other way to make tuple
"""
fruit=tuple(("apple"))
print(len(colour))
print(type(colour))

# accessing item in tuple
print(colour[0])
print(colour[1:3])
# print(colour[-1]) last value will be print
print(colour[1:]) up to end


if "green" in colour:
    print("yes there is green in list")

# travers the tuple
for i in colour:
    print(i)

# concatenat 2 tuple
more_colour=("blue","brown")
colour=more_colour+colour
print(colour)
"""
# unpaking colour

colour1, colour2, colour3 ,colour4= colour
print(colour1,colour2,colour3)