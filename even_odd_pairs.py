n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in range(n):
    if l[i]%2==0:
        a.append(l[i])
    else:
        b.append(l[i])
i=0
j=0
while i<len(a) or j<len(b):
    if i<len(a):
        print(a[i],end=" ")
        i+=1
    if j<len(b):
        print(b[j],end=" ")
        j+=1
if n%2!=0:
    print("0")