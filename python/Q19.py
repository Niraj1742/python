# write a program to print the sum from 1 to n
def sum_n(n):
    # base case
    if n==1:
        return 1
    # recursive case
    ans=n+sum_n(n-1)
    return ans
n=int(input("enter n: "))
print(sum_n(n))
