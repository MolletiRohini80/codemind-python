n=int(input())
s=list(map(int,input().split()))
a=sum(s)
d=a//n
h=0
for i in range(n):
    if s[i]>=d:
        h+=1
print(h)