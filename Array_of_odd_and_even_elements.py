n=int(input())
s=list(map(int,input().split()))
l=[]
for i in s:
    if i%2!=0:
        l.append(i)
for i in s:
    if i%2==0:
        l.append(i)
print(*l)