n=int(input())
l=list(map(int,input().split()))
k=int(input())
x=[]
s=0
for i in l:
    if i<=k:
      x.append(i)
print(sum(x))