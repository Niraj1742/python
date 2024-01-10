# take a positive integer input and tell if it is a four digit number or not.
number =int(input("Enter 4 digit number"))
if number>=1000 and number<=9999:
    print("number is 4 digit number ",number)
else:
    print("it is not a 4 digit number ")