n,m=map(int,input().split())
l=list(map(int,input().split()))
p=list(map(int,input().split()))
l,p=set(l),set(p)
c=0
for i in l:
    if i in p:
            c+=1
print(c)