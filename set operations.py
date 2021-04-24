###set operations .remove() .discard() .pop()


n = int(input())
s = set(map(int, input().split()))
m=int(input())
for i in range(m):
    arg=input().split(" ")
    if arg[0]=="pop":
        s.pop()
    elif arg[0]=="remove":
        s.remove(int(arg[1]))
    elif arg[0]=="discard":
        s.discard(int(arg[1]))
print(sum(s))

""" ---------------------------------------------------------------------------------------"""
#set .union() and .intersection() .difference() operation
m=int(input())
s1=set(map(int,input().split()))
n=int(input())
s2=set(map(int,input().split()))
#s=s1.union(s2)  #also be written as s=s1|s2
#s=s1.intersection(s2) #intersection of s1 and s2
#s=s1.difference(s2) #difference of s1 and s2
s=s1.symmetric_difference(s2) #symmetric difference of s1 and s2
print(len(s))