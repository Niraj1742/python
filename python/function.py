# write a function to print hello world
"""
def printhello():
    # body of function
    print("hello function")
printhello()

# function which take two number as input and returns their sum
def add(n1,n2):
    print("n1 ",n1)
    print("n2 ",n2)
    sum =n1+n2
    return sum
#positional arugment
# print("the sum of 2 number :",add(2,3))
# keyword argument(name argument)
print("the sum of 2 number :",add(n1=2,n2=3))
# defult argument
print("the sum of 2 number :",add(3))
# arbitrary argument
def allnum(*arg):
    sum =0
    for i in arg:
        sum+=i
    return sum
output = allnum(2,3,4,5)
print("the sum is ",output)
"""

# arbitrary argument keyword argument
def student(**kwargs):
    for x,y in kwargs.items():
        print(x,"is",y)
student(name="urfi", age=22,city="surat")
student(name="raju", age=23,city="navsari")