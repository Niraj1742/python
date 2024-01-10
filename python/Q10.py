# take 3 positive number input print the gretest number
n1=int(input("Enter Number 1 "))
n2=int(input("Enter Number 2 "))
n3=int(input("Enter Number 3 "))
"""
 if n1>n2 and n1>n3:
     print("Number 1 is greater ")
 elif n2>n1 and n2>n3:
     print("Number 2 is greater ")
 else:
     print("Number 3 is greater") 
"""
# using nested if else
if n1>n2:
   if n1>n3:
     print(n1,"is greates")
   else:
     print(n3," is greates")
else:
    print(n2,"is greates")