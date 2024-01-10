# match case
num1=int(input("Enter first number "))
num2=int(input("Enter Second number "))
operator=input("Enter the operator ")
match operator:
    case "+":
        print("addition ", num1+num2)
    case "-":
        print("Subtraction ", num1-num2)
    case "*":
        print("multiplication ", num1*num2)
    case "/":
        print("division ", num1/num2)
    case _ :
        print("enter a valid operator ")