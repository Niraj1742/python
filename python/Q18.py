# write a program to print number from n to1.
def print_N(n):
    #base case
    if n==0:
        return 0
    print(n) #if we want it in revers order
    # recursion case
    print_N(n-1)
    print(n) #if we want it in order
    
print_N(5)