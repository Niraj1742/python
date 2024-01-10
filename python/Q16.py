#  Given a dictionary in Python, write a Python program to find the sum of all items in the dictionary
# example :Input : {‘a’: 100, ‘b’:200, ‘c’:300}Output : 600
dic ={
    "a":100,
    "b":200,
    "c":300
}
print(dic.keys())
print(dic.values())
# Sum of all the value
print("the sum of all dictionary value is: ", sum(dic.values()))