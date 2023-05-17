n=int(input())
s=list(map(int,input().split()))
x=10**5
for i in range(n):
    if x>s[i]:
        x=s[i]
for i in range(1,x+1):
    c=0
    for j in range(0,n):
        if s[j]%i==0:
            c+=1
    if c==n:
       y=i
print(y)