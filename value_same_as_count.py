n=int(input())
l=list(map(int,input().split()))
c=0
b=set(l)
for i in b:
    if l.count(i)==i:
        c+=1
print(c)