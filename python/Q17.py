""" Given a string and a number N, we need to mirror the characters from the N-th position up to the length 
of the string in alphabetical order. In mirror operation, we change ‘a’ to ‘z’, ‘b’ to ‘y’, and so on.

Example:Input : N = 3

            paradox

Output : paizwlc

We mirror characters from position 3 to end"""

input_string=input("Enter String: ")
n=int(input("enter n: "))
#creating dictionary for mirror operation
alphabet ="abcdefghijklmnopqrstuvwxyz"
revers =alphabet[::-1]
dic=dict(zip(alphabet,revers))
#finding the path of string on which we will do mirror
prefix=input_string[0:n-1]
suffix=input_string[n-1:]
#finding the mirror string 
mirror =""
for i in range(0,len(suffix)):
    mirror = mirror + dic[suffix[i]]
#creating the final string
rec=prefix + mirror
print("the result is : ", rec)