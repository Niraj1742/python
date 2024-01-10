# creating string in diffrent way's
name1="niraj"
name2='singh'
name3='''we can use the triple cotes 
it work like a paraghaph string'''
"""
print(name1,name2,name3)
print(type(name1))
print(type(name2))
print(type(name3))
# indexing of string
print(name1[0])
print(name1[-1])
        
        # traversing string
#using loop
for i in name1:
    print(i)
# using list comprehension
list=[char for char in name1]
for i in list:
    print(list)
# find the lenght of string
print(len(name1))
# find  a char/substring in a string
print(name1.find("r"))
# slicing a string
print(name1[1:])
print(name1[-2: ])# negative index

# for converting lower sting to upper case string
print(name1.upper())
# for converting character to lower case
print(name1.lower())
#for capitalising the first character of my string
print(name1.capitalize())

# for stripping/removing any trailing whitespaces
str1="   hello world !     "
print(str1.strip())

# replace with substring
str1="hello niraj,how are you niraj what are you doing niraj"
print(str1.replace("niraj","NIRAJ",2))
# splitting string 
str1="ria, mia ,pia, sia tia"
list=str1.split(",",2) 
print(list)
# concatenation
str1="hello niraj"
str2="how are you niraj what are you doing niraj"
print(str1+str2)
    """
# formatting string
student="pallavi"
stud_mark=99
str1="the student name is {s},marke is {m}".format(s=student,m=stud_mark)
print(str1)