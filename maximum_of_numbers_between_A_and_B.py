n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
for i in l:
    if a<=i and b>=i:
        k.append(i)
if len(k)==0:
    print(-1)
else:
    print(max(k))