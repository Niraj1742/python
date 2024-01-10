''' Given a list in Python and provided the index of the elements, write a program to swap the two elements 
in the list. 
Examples:  
Input : List = [23, 65, 19, 90], index1 = 0, index2 = 2Output : [19, 65, 23, 90]
Input : List = [1, 2, 3, 4, 5], index1 = 1, index2 = 4Output : [1, 5, 3, 4, 2]
'''
n=int(input("enter Size of list "))
list=[]
for _ in range(n):
    num=int(input())
    list.append(num)
idx1=int(input("Enter index 1:-"))
idx2=int(input("Enter index 2:-"))
print(list)
# swapping value in idx1 and idx2
temp=list[idx1]
list[idx1]=list[idx2]
list[idx2]=temp     

print(list)