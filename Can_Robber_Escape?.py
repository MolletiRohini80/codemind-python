n=int(input())
c=0
lis=list(map(int,input().split()))
for i in range(n):
    if lis[i]%2!=0:
        c=c+1
if c<=2:
    print("YES")
else:
    print("NO")
    