n=int(input())
a=map(int,input().split())
b=map(int,input().split())
s=sum(a)
m=sum(b)
if s-m>0:
    print("0")
else:
    print(m-s)