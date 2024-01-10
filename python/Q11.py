# take a positive integer input and tell if it is divisible by 5 or 3 but not divisible by 15.
num=int(input("Enter a number "))
if num%15 == 0:
    print("this number is divisible by 15")
else:
    if num%3 == 0 or num%5 == 0:
        print("this number are divisible by 3 or 5")
    else:
        print("this number is not divisible by 3 or 5 ")
