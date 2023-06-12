n,m=map(int,input().split())
l=list(map(int,input().split()))
p=list(map(int,input().split()))
x=[]
for i in l:
    if i in p and i not in x:
        x.append(i)
print(*x)