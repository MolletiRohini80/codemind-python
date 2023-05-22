n=int(input())
s=list(map(int,input().split()))
a=sum(s)
c=a//n
b=0
for i in range(n):
    if s[i]<=c:
        b+=1
print(b)