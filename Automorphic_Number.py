n=int(input())
r=0
i=0
t=n
s=n*n
while n!=0:
    r=r+((s%10)*10**i);
    s=s//10
    n=n//10
    i+=1
if t==r:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")