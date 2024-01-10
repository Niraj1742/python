# Multiple condition using 'and' and 'or'
"""taking input of Mark in english and math comprating them """
eng_mark=int(input("Enter English mark "))
math_mark=int(input("Enter math mark "))

if eng_mark>=80 and math_mark>=80:
    print("grade A")
elif eng_mark>=80 or math_mark>=80:
    print("grade B")
else:
    print("grade c")