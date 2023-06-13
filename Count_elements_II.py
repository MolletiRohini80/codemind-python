n,m=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
e=set(l)
d=set(k)
c=0
for i in e:
    if i not in d:
        c+=1
for i in d:
    if i not in e:
        c+=1
print(c)