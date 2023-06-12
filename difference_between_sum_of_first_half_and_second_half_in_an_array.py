n=int(input())
l=list(map(int,input().split()))
s=0
c=0
for i in range(0,n//2):
    s+=l[i]
for j in range(n//2,n):
    c+=l[j]
print(abs(c-s))