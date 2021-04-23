# Write a Python program to find the second smallest number in a list


list=[]
n=int(input("Size of list : "))
for i in range(0,n):
    item=int(input())
    list.append(item)
print("List : ",list)
list.sort()
print("Second Smallest :",list[1])