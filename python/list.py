fruit=["cack","apple","banana","cherry"]
# print(fruit)
# print(type(fruit))
# print(len(fruit))
# # check if the item is persent in the list
# if "banana" in fruit:
#     print("Banana is in the fruit ")
# else:
#     print("banana is not in the list")

# access the list

# print(fruit[0])
# print(fruit[0:3])
# fruit.append("kiwi")
# print(fruit)
#
# fruit.insert(2,"kiwi")
# print(fruit)
more_fruit=["kiwi","papaya"]
fruit.extend(more_fruit)
# print(fruit)
# fruit.remove("banana")
# print(fruit)
# fruit.pop(1)
# print(fruit)

# changing/updating item
# fruit[1]="kiwi"
# print(fruit)
# fruit[1:3]="chomu"
# fruit[1:3]=["chomu"]
# print(fruit)

# print(fruit)
# fruit.sort() # by assinding oder
# fruit.sort(reverse=True)
# print(fruit)
# fruit.reverse()
# print(fruit)

# new_fruit=[fruit for fruit in fruit if "a" in fruit]
# print(new_fruit)

# copy the fruit in new_fruit
new_fruit=fruit.copy()
print(new_fruit)

new_fruit=fruit+new_fruit
print(new_fruit)