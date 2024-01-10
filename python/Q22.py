# Exception handling
a=int(input("enter a"))
b=int(input("enter b"))

try:
    result= a/b
except Exception: #we can write the name of exception
    result=None
    print("Error: cannot divide by zero")
finally:
    print("operation completed ",result)