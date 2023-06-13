n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    while(i):
        d=i%10
        s+=d
        i//=10
print(s)
        